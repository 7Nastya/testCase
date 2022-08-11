from testCase.apps.order.services import GoogleService


# decorator
def periodic_import_task():
    google_service = GoogleService()
    google_service.export_file()
