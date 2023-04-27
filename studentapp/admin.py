from django.contrib import admin
from studentapp.models import studentdatafixed, Course

# Register your models here.

admin.site.register(studentdatafixed)

admin.site.register(Course)
