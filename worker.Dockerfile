FROM python:3.8-slim
ADD . .
RUN pip install rq
RUN echo $REDIS_URL
CMD rq worker --url $REDIS_URL --verbose