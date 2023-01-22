from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from user.models import User
from .models import Teacher, Student, Course
from .forms import ProfileStudentForm, ProfileTeacherForm, CourseForm


def index(request):
    return render(request, 'main/base.html', {})

@login_required
def profile_view(request):
    user = User.objects.get(id=request.user.id)
    profile = None
    
    try:
        if user.type == 'ST':
            profile = Student.objects.get(user=user.id)
        if user.type == 'TR':
            profile = Teacher.objects.get(user=user.id)
    except ObjectDoesNotExist:
        profile = None

    context = {
        'user': user,
        'profile': profile
    }

    return render(request, 'main/profile-view.html', context)

@login_required
def profile_create(request):
    user = User.objects.get(id=request.user.id)
        
    if request.method == 'POST' and user.type == 'ST':
        student_form = ProfileStudentForm(request.POST, prefix='student')

        if student_form.is_valid():
            object = student_form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        student_form = ProfileStudentForm(prefix='student')

    if request.method == 'POST' and user.type == 'TR' and not student_form.is_valid():
        teacher_form = ProfileTeacherForm(request.POST, prefix='teacher')
        student_form = ProfileStudentForm(prefix='student')

        if teacher_form.is_valid():
            object = teacher_form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        teacher_form = ProfileTeacherForm(prefix='teacher')

    context = {
        'user': user,
        'student_form': student_form,
        'teacher_form': teacher_form,
    }

    return render(request, 'main/profile-create.html', context)

@login_required
def profile_update(request):
    user = User.objects.get(id=request.user.id)
    profile = None

    try:
        if user.type == 'ST':
            profile = Student.objects.get(user_id=request.user.id)
        if user.type == 'TR':
            profile = Teacher.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        profile = None

    if request.method == 'POST' and user.type == 'ST':
        student_form = ProfileStudentForm(request.POST, instance=profile, prefix='student')

        if student_form.is_valid():
            object = student_form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        student_form = ProfileStudentForm(instance=profile, prefix='student')

    if request.method == 'POST' and user.type == 'TR' and not student_form.is_valid():
        teacher_form = ProfileTeacherForm(request.POST, instance=profile, prefix='teacher')
        student_form = ProfileStudentForm(prefix='student')

        if teacher_form.is_valid():
            object = teacher_form.save(commit=False)
            object.user = request.user
            object.save()

            return redirect('/profile/')
    else:
        teacher_form = ProfileTeacherForm(instance=profile, prefix='teacher')

    context = {
        'student_form': student_form,
        'teacher_form': teacher_form,
    }

    return render(request, 'main/profile-update.html', context)


@login_required
def course_view(request):
    courses = Course.objects.filter(teacher=request.user.id)

    context = {
        'courses': courses
    }

    return render(request, 'main/course/view.html', context)

@login_required
def course_detail(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course
    }

    return render(request, 'main/course/detail.html', context)

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            course = Course.objects.create(
                name=form.cleaned_data['name'],
                short_name=form.cleaned_data['short_name'],
                description=form.cleaned_data['description'],
                teacher=request.user,
                hours=form.cleaned_data['hours'],
                points=form.cleaned_data['points'],
            )

            return redirect(f'/course/{course.id}')
    else:
        form = CourseForm()
    
    return render(request, 'main/course/create.html', {'form': form})

def course_update(request, id):
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            object = form.save(commit=False)
            object.teacher = request.user
            object.save()

            return redirect(f'/course/{course.id}')
    else:
        form = CourseForm(instance=course)

    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'main/course/update.html', context)

def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    return redirect(f'/course/')
