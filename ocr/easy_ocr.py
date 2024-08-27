import easyocr


easy_ocr = easyocr.Reader(['ru','en'])

class GetEasyOcrText:
    model = easy_ocr

    def get_text(image_path):
        result = GetEasyOcrText.model.readtext(image_path)
        final_text = ''
        for text in result:
            final_text += '\n' + text[1]
        
        return final_text
