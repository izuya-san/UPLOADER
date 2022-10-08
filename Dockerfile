FROM python:3.10-slim-buster

WORKDIR /root/UPLOADER-BOT-V2

COPY . .

RUN pip3 install -U -r requirements.txt

CMD ["python3","-m","bot.py"]
