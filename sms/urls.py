from django.urls import path

from sms.views import main, success

urlpatterns = [
    path("", main, name="main"),
    path("success/", success, name="success-page")
]
