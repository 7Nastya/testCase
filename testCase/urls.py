from django.contrib import admin
from django.urls import path
from django.urls import include
from testCase.apps.order import urls as order_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(order_urls)),
]
