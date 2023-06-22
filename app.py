# -*- coding: iso-8859-1 -*-
from flask import Flask, request, jsonify
import pytesseract
import cv2
import base64

#comentar antes de criar o container
path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path

app = Flask(__name__)


@app.route('/gerar', methods=['POST'])
def gerar():
    data = request.get_json()
    image = data['image']

    img_bytes = base64.b64decode(image)

    with open(".pic.jpg", "wb") as f:
        f.write(img_bytes)

    img = cv2.imread(".pic.jpg")

    try:
       # config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, lang='por')  # , config=config)
        text = text.replace("\n", " ").replace("\f", " ").strip()
    except Exception as ex:
        text = f"Requisição inválida!  {ex}"

    return jsonify(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
