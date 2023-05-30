FROM python:3.9

WORKDIR /app

COPY requeriments.txt .
COPY schema.py .
COPY conection_1.py .
COPY crud.py .

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 8000

CMD ["python", "schema.py"]