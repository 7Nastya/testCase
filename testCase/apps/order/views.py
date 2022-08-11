from django.http import HttpResponse
from django.views import View

from testCase.apps.order.services import GoogleService


class TestCaseView(View):

    def get(self, request, *args, **kwargs):
        google_service = GoogleService()
        google_service.export_file()
        return HttpResponse("OK")
