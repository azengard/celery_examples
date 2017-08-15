from celery import Celery

# app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    for x in range(1000):
        result = add.delay(x,x)
        print(result.get())
