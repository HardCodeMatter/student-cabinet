from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class Faculty(models.Model):
    name = models.CharField(_('Назва'), max_length=50)
    description = models.TextField(_('Опис'), max_length=300)
    dean = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(_('Назва'), max_length=50)
    description = models.TextField(_('Опис'), max_length=300)
    head = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField(_('Teacher\'s office'), max_length=5, blank=True, null=True)

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    class ScientificDegree(models.TextChoices):
        DOCTOR = 'Доктор наук', _('Доктор наук')
        CANDIDATE = 'Кандидат наук', _('Кандидат наук')
    
    scientific_degree = models.CharField(
        _('Науковий ступінь'),
        max_length=13,
        choices=ScientificDegree.choices
    )

    class AcademicStatus(models.TextChoices):
        RESEARCH_OFFICER = 'Ст. науковий дослідник', _('Ст. науковий дослідник')
        DOCENT = 'Доцент', _('Доцент')
        PROFESSOR = 'Професор', _('Професор')

    academic_status = models.CharField(
        _('Вчене звання'),
        max_length=22,
        choices=AcademicStatus.choices
    )

    def __str__(self):
        return f'{self.user}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(_('Specialty'), max_length=30, blank=True, null=True)
    educational_program = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_educational_program', null=True, default=None)
    
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department', null=True)

    EDUCATIONAL_LEVEL_CHOICES = [
        ('Бакалавр', 'Бакалаврат'),
        ('Магістр', 'Магістратура'),
        ('Докторант', 'Докторантура')
    ]
    educational_level = models.CharField(
        _('Educational level'), 
        max_length=30,
        choices=EDUCATIONAL_LEVEL_CHOICES, 
        blank=True, 
        null=True
    )
    
    group = models.CharField(_('Group'), max_length=6, blank=True, null=True)
    entry_date = models.DateField(_('Entry date'), blank=True, null=True)

    EDUCATION_FORM_CHOICES = [
        ('Денна', 'Денна'),
        ('Заочна', 'Заочна')
    ]
    education_form = models.CharField(
        _('Education form'), 
        max_length=10, 
        choices=EDUCATION_FORM_CHOICES, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f'{self.user}'


class Course(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    short_name = models.CharField(_('Short name'), max_length=10)
    description = models.CharField(_('Description'), max_length=300, blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.IntegerField(_('Hours'))
    points = models.IntegerField(_('Points'))

    class CourseType(models.TextChoices):
        GENERAL_TRAINING = 'Дисципліна загальної підготовки', _('Дисципліна загальної підготовки')
        PROFESSIONAL_TRAINING = 'Дисципліна професійної підготовки', _('Дисципліна професійної підготовки')
        ELECTIVE_DISCIPLINE = 'Вибіркова дисципліна', _('Вибіркова дисципліна')
    
    course_type = models.CharField(
        _('Тип дисципліни'),
        max_length=33,
        choices=CourseType.choices,
        null=True,
    )

    def __str__(self):
        return f'{self.name}'

class Membership(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    points = models.IntegerField(_('Бали'), blank=True, null=True)


class Message(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(('Повідомлення'), max_length=500)
