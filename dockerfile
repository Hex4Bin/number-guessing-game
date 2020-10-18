FROM python:3.9.0-alpine3.12
WORKDIR .
COPY . .
RUN python -m pip install --upgrade pip
EXPOSE 80
CMD ["python", "./guess_game.py"]