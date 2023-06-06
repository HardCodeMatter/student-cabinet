from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from user.models import User
from .models import Teacher, Student, Course, Membership, Message
from .forms import ProfileStudentForm, ProfileTeacherForm, CourseForm, CoursePointForm, CourseMessageForm


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
    try:
        student = Student.objects.get(user=request.user.id)
    except ObjectDoesNotExist:
        student = None

    courses = Course.objects.filter(teacher=request.user.id)
    memberships = Membership.objects.filter(student=student)

    context = {
        'courses': courses,
        'memberships': memberships,
    }

    return render(request, 'main/course/view.html', context)

@login_required
def course_detail(request, id):
    course = Course.objects.get(id=id)
    student_list = Membership.objects.filter(course_id=id)
    
    try:
        membership = None

        if request.user.type == 'ST':
            student = Student.objects.get(user=request.user.id)
            membership = Membership.objects.filter(student=student, course=course)
    except ObjectDoesNotExist:
        print('Object doen\'t exist!')

    context = {
        'course': course,
        'membership': membership,
        'student_list': student_list,
    }

    return render(request, 'main/course/detail.html', context)

@login_required
def course_create(request):
    if request.user.type == 'ST':
        return redirect('/course/')

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

@login_required
def course_update(request, id):
    if request.user.type == 'ST':
        return redirect('/course/')

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

@login_required
def course_delete(request, id):
    if request.user.type == 'ST':
        return redirect('/course/')

    course = Course.objects.get(id=id)
    course.delete()

    return redirect(f'/course/')


@login_required
def course_list(request):
    if request.user.type == 'TR':
        return redirect('/course/')

    student = Student.objects.get(user=request.user.id)
    courses = Course.objects.all()

    available_courses = []

    membership = None

    for course in courses:
        try:
            membership = Membership.objects.get(student=student, course=course)
        except ObjectDoesNotExist:
            print('Object was not found!')

        if membership != None and course != membership.course:
            available_courses.append(course)

    context = {
        'available_courses': available_courses,
    }

    return render(request, 'main/course/list.html', context)

@login_required
def course_add(request, id):
    if request.user.type == 'TR':
        return redirect(f'/course/{id}')

    student = Student.objects.get(user=request.user.id)
    course = Course.objects.get(id=id)

    Membership.objects.create(
        student=student,
        course=course
    )

    return redirect(f'/course/{course.id}/')

@login_required
def course_set_point(request, course_id, student_id):
    course = Course.objects.get(id=course_id)
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = CoursePointForm(request.POST)

        if form.is_valid():
            Membership.objects.filter(
                course=course, student=student_id
            ).update(
                points=form.cleaned_data['points']
            )

            return redirect(f'/course/{course.id}/')
    else:
        form = CoursePointForm()

    context = {
        'form': form,
        'course': course,
        'student': student,
    }
    
    return render(request, 'main/course/set_point.html', context)

@login_required
def course_grade_list(request):
    student = Student.objects.get(user=request.user)
    memberships = Membership.objects.filter(student=student)

    context = {
        'memberships': memberships,
    }

    return render(request, 'main/course/grade_list.html', context)


@login_required
def course_message_list(request):
    try:
        memberships = None
        courses = None

        if request.user.type == 'ST':
            student = Student.objects.get(user=request.user.id)
            memberships = Membership.objects.filter(student=student)
        elif request.user.type == 'TR':
            courses = Course.objects.filter(teacher=request.user)
    except ObjectDoesNotExist:
        print('Об\'єкт не знайдено!')

    context = {
        'memberships': memberships,
        'courses': courses,
    }

    return render(request, 'main/course/message_list.html', context)

@login_required
def course_message(request, id):
    course = Course.objects.get(id=id)
    memberships = Membership.objects.filter(course=course)
    messages = Message.objects.filter(course=course).order_by('-id')

    if request.method == 'POST':
        form = CourseMessageForm(request.POST)

        if form.is_valid():
            Message.objects.create(
                course = course,
                author = request.user,
                message = form.cleaned_data['message'],
            )

            return redirect(f'/course/{course.id}/message/')
    else:
        form = CourseMessageForm()

    context = {
        'course': course,
        'messages': messages,
        'memberships': memberships,
        'form': form,
    }

    return render(request, 'main/course/message.html', context)
