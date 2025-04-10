FROM python:3.9
WORKDIR /app

COPY . .

RUN pip install flask && \
    apt-get update && \
    apt-get install -y cron && \
    chmod +x /app/backup.sh && \
    crontab /app/crontab.txt

EXPOSE 5000
CMD cron && python app.py




