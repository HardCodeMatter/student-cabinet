from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from user.models import User
from .models import Teacher, Student


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


    return render(request, 'main/profile-view.html', {'profile': profile})

def profile_create(request):
    return render(request, 'main/profile-create.html', {})
