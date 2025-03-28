from django.db import models


# Create your models here.
class Job(models.Model):
    WORK_TYPES = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Office', 'Office'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    work_type = models.CharField(max_length=10, choices=WORK_TYPES)

    def __str__(self):
        return f"{self.title} at {self.company_name} ({self.work_type})"
