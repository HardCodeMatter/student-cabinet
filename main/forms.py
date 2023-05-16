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

class ProfileTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'scientific_degree',
            'academic_status',
            'office',
        )

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'name',
            'short_name',
            'description',
            'hours',
            'points',
        )

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
