from skills.models import Skill
from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return HttpResponse("Home")

def skills(request):
    skills = Skill.objects.order_by('name')[:5]
    context = {'skills': skills}
    return render(request, 'skills/index.html', context)