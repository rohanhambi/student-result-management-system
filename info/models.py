from django.db import models
from django.contrib.auth.models import AbstractUser , UserManager

# Create your models here.
class Meta:
        app_label = 'info'
class CustomUserManager(UserManager):
    pass
class CustomUser(AbstractUser):
    object = CustomUserManager()
class Student(models.Model):
    select_gender = (
        ('Male','Male'),
        ('Female','Female'),
    )
    student_name = models.CharField(max_length=100)
    student_htno = models.CharField(max_length=20)
    student_email = models.EmailField(max_length=100)
    student_gemder = models.CharField(max_length=8,choices=select_gender)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null = True)
    def __str__(self):
        return student_name


class StudentClass(models.Model):
    select_section = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=10,choices=select_section)
    def __str__(self):
        return self.class_name
class Subjects(models.Model):
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name
class Result(models.Model):
    status = (
        ('Fail','Fail'),
        ('Pass','Pass'),
    )
    select_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student,on_delete=models.CASCADE)
    result_status = models.CharField(max_length=10,choices=status)
    def __str__(self):
        return self.select_class.class_name