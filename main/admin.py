from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'scientific_degree', 'academic_status',)
    list_filter = ('user', 'scientific_degree', 'academic_status',)
    
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Teacher\'s information', {'fields': (
            'scientific_degree', 
            'academic_status',
            'office',
        )}),
    )
    
    search_fields = ('user', 'scientific_degree', 'academic_status',)
    ordering = ('user',)
