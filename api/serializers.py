from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resume
        fields = ['id', 'tittle','file', 'created_at']
        read_only_fields = ['created_at',]
