FROM python:3.12

ADD v1.py .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./v1.py"]
