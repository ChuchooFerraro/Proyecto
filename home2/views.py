from django.shortcuts import render
from django.db.models import Q

from course.models import Course
from user.models import Avatar

# Create your views here.


def index(request):
    courses = Course.objects.all()

    context_dict={
    'courses': courses,
    }
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home2/cursos.html"
    )