
from pickle import GET
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


from course.models import Course

class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"

    def get_queryset(self):  # new
        
        if self.request.GET.get("Q"):
            query = self.request.GET.get("Q")
            courses = Course.objects.filter(
                Q(name__icontains=query) | Q(code__icontains=query)
            )
            
        else:
            courses= Course.objects.all()
        return courses

class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    fields = ['name', 'code', 'description']

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    success_url = reverse_lazy('course:course-list')
    fields = ['name', 'code', 'description']


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('course:course-list')
    fields = ['name', 'code', 'description']


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('course:course-list')



    


def cursos_search(request):

    courses= Course.objects.all()
    context_dict = {'courses': courses}

    if request.GET["all_search"]:
        search_param = request.GET["all_search"]
        query = Q(curso__contains=search_param)
        query.add(Q(camada__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        
        context_dict = {
            'courses': courses
        }

    return render(
        request=request,
        context=context_dict,
        template_name="course/course_search.html",
    )
