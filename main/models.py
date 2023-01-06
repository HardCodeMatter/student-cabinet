from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField(_('Teacher\'s office'), max_length=5, blank=True, null=True)

    class ScientificDegree(models.TextChoices):
        DOCTOR = 'DS', _('Doctor of Sciences')
        CANDIDATE = 'CS', _('Candidate of Sciences')
    
    scientific_degree = models.CharField(
        _('Scientific degree'),
        max_length=2,
        choices=ScientificDegree.choices
    )

    class AcademicStatus(models.TextChoices):
        RESEARCH_OFFICER = 'RO', _('Senior Research Officer')
        DOCENT = 'DC', _('Docent')
        PROFESSOR = 'PR', _('Professor')

    academic_status = models.CharField(
        _('Academic status'),
        max_length=2,
        choices=AcademicStatus.choices
    )

    def __str__(self):
        return f'{self.user}'
