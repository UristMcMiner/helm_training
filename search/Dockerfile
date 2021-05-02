FROM python:3.9.4-alpine3.13

COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD python -u cache_update.py