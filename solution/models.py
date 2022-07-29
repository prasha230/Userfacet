from django.db import models

# Create your models here.
class scheduled_class(models.Model):
    student_name = models.CharField('Student Name', max_length=120)
    student_email = models.EmailField('Student Email',blank=False)
    weekday = models.CharField('Weekday', max_length=120)
    start_time = models.TimeField('Start Time')
    end_time = models.TimeField('End Time')
    date = models.DateField('Date')