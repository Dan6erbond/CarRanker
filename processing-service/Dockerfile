FROM python:3.9.2
RUN mkdir -p /app/
WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "/app/entrypoint.sh" ]
