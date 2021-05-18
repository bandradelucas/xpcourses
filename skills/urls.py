from django.urls import path

from . import views

urlpatterns = [
    # ex: /skills/
    path('', views.skills, name="skills"),
]