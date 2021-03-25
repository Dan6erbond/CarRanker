FROM python:3.9.2

RUN mkdir -p /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV HOST=0.0.0.0
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["./wait-for-it.sh", "db:5432", "--", "./entrypoint.sh"]
