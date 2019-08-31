from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_htno','student_email',)
    search_field = ('student_htno')
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('class_name','section')
    search_field = ('class_name')
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','subject_code')
    search_field = ('subject_name','subject_code')
class ResultAdmin(admin.ModelAdmin):
    list_display = ('select_class','select_student')
    search_field = ('select_class')
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentClass,StudentClassAdmin)
admin.site.register(Subjects,SubjectAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(CustomUser,CustomUserAdmin)