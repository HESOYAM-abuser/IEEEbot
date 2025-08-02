FROM python:3.13.5-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY bot ./bot
COPY .env ./.env

CMD ["python", "bot/bot.py"]
