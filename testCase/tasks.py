from testCase.apps.order.services import GoogleService
from testCase.celery import app


@app.task()
def test_case():
    google_service = GoogleService()
    google_service.export_file()
