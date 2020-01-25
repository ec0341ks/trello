from django.urls import path
from . import views

app_name = 'trello'

url_pattterns = [
    path("", views.index, name="index"),
]
