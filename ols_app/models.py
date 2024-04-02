from django.db import models

# Create your models here.

class Course(models.Model):

    course_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    instructor = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    price_bdt = models.FloatField()

    
    def __str__(self):
        return f'{self.title} by Mr. {self.instructor}'

class Enrollment(models.Model):

    enrollment_id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student_name} enrolled in {self.course.title} course'

    