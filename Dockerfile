FROM python:3.9-alpine3.16

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "-m" , "flask", "--app", "city_redis", "run", "--host=0.0.0.0"]

