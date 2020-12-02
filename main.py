from redis import Redis
from rq import Queue
from processor import processor_function
from os import environ
from time import sleep


def main():
    redis_host = environ.get('REDIS_HOST')
    redis_port = environ.get('REDIS_PORT')
    queue = Queue(connection=Redis(host=redis_host, port=redis_port))
    print(f"Connected to Redis at redis://{redis_host}:{redis_port}.")

    for i in range(1, 5):
        job = queue.enqueue(processor_function)
        print(f"Enqueued Job id={job.id}, status={job.get_status()}.")
        print("Waiting 5 seconds...")
        sleep(5)


if __name__ == '__main__':
    print("Started producer.")
    main()
