import time

from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379")
app.config_from_object("celeryconfig")


@app.task
def add(x, y):
    time.sleep(5)
    result = x * y
    return result


# celery -A tasks worker -l info - это комманда для запуска celery в терминале
