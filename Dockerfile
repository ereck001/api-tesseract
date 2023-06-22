FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

COPY por.traineddata .

RUN apt update

RUN  apt install tesseract-ocr -y

RUN  apt install libgl1-mesa-glx -y

RUN pip install --no-cache-dir -r requirements.txt

RUN cp por.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
