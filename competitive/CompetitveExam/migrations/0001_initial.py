# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitveExamModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stream', models.CharField(default=b'Arts', max_length=400, choices=[(b'Arts', b'Arts'), (b'Science', b'Science'), (b'Engineering', b'Engineering')])),
                ('career_choice', models.CharField(default=b'Artist', max_length=400, choices=[(b'Artist', b'Artist'), (b'Doctor', b'Doctor'), (b'Engineer', b'Engineer')])),
                ('subjects', models.TextField(default=b'Maths', help_text=b'Enter Subjects', max_length=400)),
                ('competitive_exam', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('year_of_publication', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
