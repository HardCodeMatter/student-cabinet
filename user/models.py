from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True, max_length=150)
    
    first_name = models.CharField(('first name'), max_length=30)
    middle_name = models.CharField(('middle name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    date_of_birth = models.DateField(('date of birth'), blank=True, null=True)
    phone = models.IntegerField(('phone number'), blank=True, null=True)
    photo = models.ImageField(('user photo'), upload_to='photo', blank=True, null=True)
    
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_staff = models.BooleanField(('staff'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_verified = models.BooleanField(('verified'), default=False)

    GROUP_CHOICES = [
        ('ST', 'Student'),
        ('TR', 'Teacher'),
    ]
    group = models.CharField(
        max_length=2, 
        choices=GROUP_CHOICES, 
        default='ST'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name',
    ]

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    @property
    def is_admin(self):
        "Is the user an admin member?"
        return self.is_staff
