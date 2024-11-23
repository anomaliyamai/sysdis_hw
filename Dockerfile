FROM python:3.10
LABEL authors="olegafanasev"
COPY project/ /project/
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /project
CMD ["python", "main.py"]
