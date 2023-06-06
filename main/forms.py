from django import forms
from .models import Student, Teacher, Course, Membership, Message


class ProfileStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'specialty',
            'educational_program',
            'educational_level',
            'group',
            'education_form',
            'entry_date',
        )
        labels = {
            'specialty': ('Спеціальність'),
            'educational_program': ('Освітня програма'),
            'educational_level': ('Освітній рівень'),
            'group': ('Група'),
            'education_form': ('Форма навчання'),
            'entry_date': ('Дата вступу'),
        }


class ProfileTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'scientific_degree',
            'academic_status',
            'office',
        )
        labels = {
            'scientific_degree': ('Науковий ступінь'),
            'academic_status': ('Вчене звання'),
            'office': ('Кабінет'),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'name',
            'short_name',
            'description',
            'course_type',
            'hours',
            'points',
        )
        labels = {
            'name': ('Назва'),
            'short_name': ('Коротка назва'),
            'description': ('Опис'),
            'course_type': ('Тип курсу'),
            'hours': ('Кількість годин'),
            'points': ('Кількість балів'),
        }


class CoursePointForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = (
            'points',
        )


class CourseMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'message',
        )
