import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

from saiga.instructions import DataTimeExtract, DataTimeExtractDouble, DataTimeExtractNew


class InstructModel:
    def __init__(
        self,
        model,
        tokenizer, 
        gen_config,
        system_prompt,
        response_template
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.gen_config = gen_config
        self.response_template = response_template
        self.system_prompt = system_prompt

    def _get_prompt(self, text):
        final_text = self.system_prompt
        final_text += text
        final_text += self.response_template
        return final_text.strip()
    
    def generate(self, text):
        prompt = self._get_prompt(text)
        data = self.tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
        data = {k: v.to(self.model.device) for k, v in data.items()}
        output_ids = self.model.generate(
            **data,
            generation_config=self.gen_config
        )[0]
        output_ids = output_ids[len(data["input_ids"][0]):]
        output = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        return output.strip()


MODEL = 'IlyaGusev/saiga_llama3_8b'
MODEL_PATH = './saiga/HF_model'
TEMPERATURE = 0.0001
MAX_NEW_TOKENS = 128
REVISION = '1cc945d4ca2c7901cf989e7edaac52ab24f1a7dd'
DEVICE = 'cuda'

try:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        load_in_8bit=True,
        torch_dtype=torch.float16,
        device_map=DEVICE
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_fast=False)
    gen_config = GenerationConfig.from_pretrained(MODEL_PATH)
except Exception as e:
    print(e)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL,
        revision=REVISION,
        load_in_8bit=True,
        torch_dtype=torch.float16,
        device_map=DEVICE,
        cache_dir=MODEL_PATH
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(MODEL, use_fast=False, cache_dir=MODEL_PATH)
    gen_config = GenerationConfig.from_pretrained(MODEL, cache_dir=MODEL_PATH)

gen_config.temperature = TEMPERATURE
gen_config.max_new_tokens = MAX_NEW_TOKENS

extractor = InstructModel(model, tokenizer, gen_config, DataTimeExtractNew.SYSTEM_PROMPT, DataTimeExtractNew.RESPONSE_TEMPLATE)