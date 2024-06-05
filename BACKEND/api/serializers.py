# serializers.py
from rest_framework import serializers
from .models import project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('id', 'project_name', 'start_date', 'end_date', 'comments', 'status')

