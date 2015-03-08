from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] # Gives a form with pub_date first and question_text next;
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]


admin.site.register(Question,QuestionAdmin)

# Register your models here.
