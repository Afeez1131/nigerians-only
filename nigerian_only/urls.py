from django.urls import path

from nigerian_only import views

urlpatterns = [
    path("", views.home, name="home"),
]
