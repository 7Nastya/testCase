from django.urls import path
from . import views

urlpatterns = [
    path('test_case/', views.TestCaseView.as_view(), name='test_case'),
    path('test_api/', views.TestAPIView.as_view(), name='test_case'),
]
