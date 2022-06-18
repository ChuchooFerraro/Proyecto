import random
import string
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render
from course.models import Course
from profesor.models import Profesor
from profesor.forms import ProfesorForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def profesor_list(request):
    profesors = Profesor.objects.all()
    courses = Course.objects.all()
    context_dict = {
        'profesors': profesors,
        'courses' : courses 
    }

    return render(
        request=request,
        context=context_dict,
        template_name="profesor/profesor_list.html"
    )

class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = reverse_lazy('profesor:profesor-list')
    fields = '__all__'

class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = reverse_lazy('profesor:profesor-list')
    fields = '__all__'



@login_required
def update_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)

    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor.name = data['name']
            profesor.last_name = data['last_name']
            profesor.email = data['email']
            profesor.profession = data['profession']
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="profesor/profesor_list.html"
            )

    profesor_form = ProfesorForm(model_to_dict(profesor))
    context_dict = {
        'profesor': profesor,
        'profesor_form': profesor_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='profesor/profesor_form.html'
    )


@login_required
def delete_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)
    if request.method == 'POST':
        profesor.delete()

        profesors = Profesor.objects.all()
        context_dict = {
            'profesors': profesors
        }
        return render(
            request=request,
            context=context_dict,
            template_name="profesor/profesor_list.html"
        )

    context_dict = {
        'profesor': profesor,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='profesor/profesor_confirm_delete.html'
    )
