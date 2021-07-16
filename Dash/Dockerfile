  
FROM python:3.8-alpine

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3" , "main.py"]
© 2021 GitHub, Inc.
