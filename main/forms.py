from django import forms
from .models import Student


class ProfileStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'specialty',
            'educational_program',
            'educational_level',
            'group',
            'education_form',
            'entry_date'
        )
