from django.urls import path

from . import views

urlpatterns = [
    path('', views.tracker, name="tracker"),
    path('update', views.update, name="update"),
]