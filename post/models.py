from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Job(models.Model):
    WORK_TYPE_CHOICES = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Office', 'Office'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs', default=1)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f"{self.title} - {self.company_name}"
