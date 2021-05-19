from xpcourse.views import getLvl
from skills.models import Skill
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Home")

def skills(request):
    skills = Skill.objects.order_by('name')[:5]
    context = {'skills': skills}
    
    return render(request, 'skills/index.html', context)

def updateSkill(request, skill_id):
    if request.method == 'POST':
        skill = Skill.objects.get(pk=skill_id)
        user = request.user
        user.xp = user.xp + skill.xp
        
        user.lvl = getLvl(user.xp)

        user.save()

        userUp = {
            "lvl": user.lvl,
            "xp": user.xp
        }

        return JsonResponse(userUp, safe=False)