from django.contrib import admin
from .models import Faculty, Department, Teacher, Student


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dean',)
    list_filter = ('name', 'dean',)

    fieldsets = (
        (None, {'fields': ('name', 'dean', 'description',)}),
    )

    search_fields = ('name', 'dean',)
    ordering = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'faculty',)
    list_filter = ('name', 'head', 'faculty',)

    fieldsets = (
        (None, {'fields': ('name', 'head', 'faculty', 'description',)}),
    )

    search_fields = ('name', 'head', 'faculty',)
    ordering = ('name',)


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


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'group', 'educational_level', 'education_form')
    list_filter = ('user', 'specialty', 'group', 'educational_level', 'education_form')

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Student\'s information', {'fields': (
            'specialty',
            'educational_program',
            'educational_level',
            'group',
            'education_form',
            'entry_date',
        )})
    )

    search_fields = ('user', 'group', 'specialty')
    ordering = ('specialty',)
