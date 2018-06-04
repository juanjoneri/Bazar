from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("projects", views.projects),
    path("experience", views.experience),
    path("education", views.education),
    path("resume", views.resume),
    path("transcript", views.transcript),
]