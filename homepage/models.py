from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    detail = models.TextField(blank=False)
    classroom = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name