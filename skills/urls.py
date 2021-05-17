from django.urls import path

from . import views

urlpatterns = [
    # ex: /skills/
    path('', views.skills, name="skills"),
    
    # ex: /categories/5/
    path('<int:skill_id>/', views.skill, name='skill'),
]