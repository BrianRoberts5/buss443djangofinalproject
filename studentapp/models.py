from django.db import models

# Create your models here.

# Student ID,First Name,Last Name,Major,Year,GPA



class studentdatafixed(models.Model):
    StudentID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Major = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
    
class studentdata(models.Model):
    Chicken = models.IntegerField()
    
class Course(models.Model):
    CourseID = models.IntegerField(primary_key=True)
    CourseTitle = models.CharField(max_length=50)
    CourseName = models.CharField(max_length=50)
    CourseSectionCode = models.IntegerField()
    CourseDepartment = models.CharField(max_length=50)
    Instructor = models.CharField(max_length=50)