FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "src/main.py", "--port", "80" ]