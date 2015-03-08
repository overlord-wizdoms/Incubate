from django.contrib import admin
from CompetitveExam.models import CompetitveExamModel

class CompetetitveModelAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] # Gives a form with pub_date first and question_text next;
    fieldsets = [
        ('Stream',               {'fields': ['stream']}),
        ('Career Choice',               {'fields': ['career_choice','competitive_exam']}),
        ('Subjects', {'fields': ['subjects'],'classes':['collapse']}),
        ('Books', {'fields': ['title','author','publisher','year_of_publication','ISBN'], 'classes':['collapse']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]


admin.site.register(CompetitveExamModel,CompetetitveModelAdmin)

# Register your models here.
