from typing import Annotated

from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel

from saiga.model import extractor
from ocr.easy_ocr import GetEasyOcrText
from ocr.doc_tr import GetDocTrText

class ModelOutput(BaseModel):
    output: str

doc_tr = GetDocTrText
easy_ocr = GetEasyOcrText
app = FastAPI()

# @app.post("/uploadfile_easyocr/")
# async def easyocr_file(file: UploadFile):
#     try:
#         contents = await file.read()
#         text = easy_ocr.get_text(contents)
#         output = extractor.generate(text)
#         return ModelOutput(output=output)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.post("/uploadfile_doctr/")
# async def doctr_file(file: UploadFile):
#     try:
#         contents = await file.read()
#         text = doc_tr.get_text(contents)
#         output = extractor.generate(text)
#         return ModelOutput(output=output)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/uploadfile_double_ocr/")
async def double_file(file: UploadFile):
    try:
        contents = await file.read()
        text_1 = 'OCR_1: ///' + easy_ocr.get_text(contents) + '\n'
        text_2 = '/// OCR_2: ///' + doc_tr.get_text(contents) + ''
        final_text = text_1 + text_2
        output = extractor.generate(final_text)
        return ModelOutput(output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/uploadfile_bytes/")
async def bytes_file(file: Annotated[bytes, File()]):
    try:
        text_1 = 'OCR_1: ///' + easy_ocr.get_text(file) + '\n'
        text_2 = '/// OCR_2: ///' + doc_tr.get_text(file) + ''
        final_text = text_1 + text_2
        output = extractor.generate(final_text)
        return ModelOutput(output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))