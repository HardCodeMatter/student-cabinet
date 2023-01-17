from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from user.models import User
from .models import Teacher, Student
from .forms import ProfileStudentForm


def index(request):
    return render(request, 'main/base.html', {})

def profile_view(request):
    user = User.objects.get(id=request.user.id)
    profile = None

    try:
        if user.type[0]:
            profile = Student.objects.get(user=user.id)
        elif user.type[1]:
            profile = Teacher.objects.get(user=user.id)
    except ObjectDoesNotExist:
        profile = None

    context = {
        'profile': profile
    }

    return render(request, 'main/profile-view.html', context)

def profile_create(request):
    if request.method == 'POST':
        form = ProfileStudentForm(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        form = ProfileStudentForm()

    context = {
        'form': form
    }

    return render(request, 'main/profile-create.html', context)

def profile_update(request):
    student = Student.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = ProfileStudentForm(request.POST, instance=student)

        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        form = ProfileStudentForm(instance=student)

    context = {
        'form': form
    }

    return render(request, 'main/profile-update.html', context)
