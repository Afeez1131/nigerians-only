from django.urls import path

from nigerian_only import views

urlpatterns = [
    path("", views.home, name="home"),
    path("restricted", views.restricted_view, name="restricted")
]
