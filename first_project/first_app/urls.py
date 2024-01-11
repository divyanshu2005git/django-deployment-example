from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.index,name="index"),
    path("form/", views.form_name_view,name="form"),
]
