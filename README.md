# Incubate
python manage.py makemigrations CompetitveExam
python manage.py sqlmigrate CompetitveExam 0001
python manage.py migrate
python manage.py create superuser

