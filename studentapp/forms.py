from django import forms
from django.db import models


class enrollmentform(forms.Form):
    student = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(enrollmentform, self).__init__(*args, **kwargs)
        self.fields['studentdata'].choices = [(studentdata.id, f"{studentdata.first_name} {studentdata.last_name}") for studentdata in enrollmentform.objects.all()]
        self.fields['course'].choices = [(course.id, course.name) for course in Course.objects.all()]
