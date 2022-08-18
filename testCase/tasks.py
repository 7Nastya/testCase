from testCase.apps.order.services import GoogleService
from testCase.celery import app


@app.task()
def test_case():
    GoogleService.export_file()


@app.task
def check():
    print('I am checking your stuff')
