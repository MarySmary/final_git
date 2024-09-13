FROM python:3.8-slim
 
WORKDIR /app 
 
RUN pip install psycopg2-binary

COPY . . 
 
CMD ["python", "app.py"]
