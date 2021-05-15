from django.urls import path

from .views import OlaMundo

urlpatterns = [
    path('', OlaMundo.as_view(), name='index'),
]
