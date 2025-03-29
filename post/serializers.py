from rest_framework import serializers
from .models import Job  # Adjust if your model is in a different file


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'work_type']
