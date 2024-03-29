FROM python:3.10.10-bullseye
WORKDIR /bot


COPY requirements.txt /bot/
RUN pip install -r requirements.txt
COPY . /bot
CMD python app.py