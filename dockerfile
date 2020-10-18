FROM python:3.9.0-alpine3.12
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip
CMD ["python", "./guess_game.py"]