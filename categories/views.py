from django.http.request import HttpRequest
from skills.models import Skill
from django.db.models.query import Prefetch
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirectBase
from categories.models import Category


def index(request):
    return HttpResponse("Home")

def categories(request):
    categories = Category.objects.order_by('name')[:10
    ]
    context = {'categories': categories}
    
    return render(request, 'categories/index.html', context)

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    context = {'category': category}

    return render(request, 'categories/category.html', context)