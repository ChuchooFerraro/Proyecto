from django.shortcuts import render
from django.db.models import Q
from datetime import datetime as dt
from course.models import Course
from user.models import Avatar

# Create your views here.

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}



def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    courses = Course.objects.all()
    context_dict.update({
        'courses': courses,
        'time' : dt.now(),
    })
    print('context_dict: ', context_dict)


    return render(
        request=request,
        context=context_dict,
        template_name="home2/home2.html"
    )


def about_us(request):
    courses = Course.objects.all()
    context_dict={
        'courses': courses,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="home2/about_us.html"
    )

def error_404(request, exception, template_name='home2/404.html'):
    return render(request, 'home2/404.html')