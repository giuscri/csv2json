FROM python:alpine

RUN pip install pytest

WORKDIR /app
COPY . .

RUN pytest .

FROM python:alpine

WORKDIR /app
COPY --from=0 /app/main.py .

CMD python main.py
