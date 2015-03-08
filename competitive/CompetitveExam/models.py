from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class CompetitveExamModel(models.Model):
    ARTS = 'Arts'
    SCIENCE = 'Science'
    ENGINEERING = 'Engineering'
    STREAM = (
        (ARTS, 'Arts'),
        (SCIENCE, 'Science'),
        (ENGINEERING, 'Engineering'),
    )
    stream = models.CharField(max_length=400,choices=STREAM,default=ARTS)
    ARTIST = 'Artist'
    DOCTOR = 'Doctor'
    ENGINEER = 'Engineer'
    CAREERCHOICE = (
        (ARTIST, 'Artist'),
        (DOCTOR, 'Doctor'),
        (ENGINEER, 'Engineer'),
    )
    career_choice = models.CharField(max_length=400,choices=CAREERCHOICE,default=ARTIST)
    subjects = models.TextField(max_length=400,help_text='Enter Subjects',default='Maths')
    competitive_exam = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year_of_publication = models.CharField(max_length=200)
    ISBN  = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.career_choice

    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)

