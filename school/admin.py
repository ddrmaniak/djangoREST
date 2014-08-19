from django.contrib import admin
from school.models import Teacher, Student


class StudentInline(admin.TabularInline):
    model = Student


class TeacherAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [StudentInline, ]

admin.site.register(Teacher, TeacherAdmin)


class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'GPA', 'teacher']

admin.site.register(Student, StudentAdmin)


# Register your models here.
