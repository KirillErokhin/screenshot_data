from doctr.io import DocumentFile
from doctr.models import ocr_predictor


doc_tr = ocr_predictor(pretrained=True)

class GetDocTrText:
    model = doc_tr

    def get_text(image_path):
        doc = DocumentFile.from_images(image_path)
        result = GetDocTrText.model(doc)
        final_text = ''
        for line in result.export()['pages'][0]['blocks'][0]['lines']:
            for word in line['words']:
                final_text += '\n' + word['value']
        
        return final_text
