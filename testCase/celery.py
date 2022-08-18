import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testCase.settings')

app = Celery('testCase', broker='redis://localhost:6379/0', include=['testCase.tasks'])
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-minute': {
        'task': 'testCase.tasks.test_case', #'testCase.tasks.check',
        'schedule': 10.0  # crontab()
    }
}
