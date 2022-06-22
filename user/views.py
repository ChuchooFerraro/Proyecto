
import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from .models import User


from user.forms import UserRegisterForm, UserEditForm, AvatarForm
from user.models import Avatar


def register(request):
    print("entraste en register")
    if request.method == 'POST':
        print("ES UN POST")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("ES UN FORM VALIDO")
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("user:user-login")
    messages.error(request,"Algo anduvo mal, vuelve a intentarlo")
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home2:index")

        return render(
            request=request,
            context={'form': form},
            template_name="user/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="user/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("user:user-login")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Modificado correctamente!")
            return redirect('user:user-update')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="user/user_form.html",
    )

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        print("URL Avatar: ",avatars[0].image.url)
        return {"url": avatars[0].image.url}
    return {}

@login_required
def avatar_load(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}

    print("request de avatar: " , request)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('user:avatar-load')
    
    form= AvatarForm()
    context_dict.update({
        'form': form,
    })
    print("Contexto: ",context_dict)
    
    return render(
        request=request,
        context=context_dict,
        template_name="user/avatar_form.html",
    )
