from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    # ex: /categories/
    path('', views.categories, name="categories"),
    
    # ex: /categories/5/
    path('<int:category_id>/', views.category, name='category'),
    path('<int:skill_id>/', views.updateSkill, name='updateSkill'),
]