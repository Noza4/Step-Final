from django.contrib.auth.models import User
from django.db import models

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


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'user')

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"