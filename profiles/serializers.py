from django.db import models
from rest_framework import serializers
from .models import Profile, Resume

class ProfileSerializer(serializers.ModelSerializer):
    resume_path = serializers.SerializerMethodField()
    is_deleted = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Profile
        exclude = ()
    
    def get_resume_path(self, obj):
        return obj.latest_resume.file.url if obj.latest_resume else None

class ResumeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    is_current = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        exclude = ('profile',)
    
    def get_is_current(self, obj):
        return obj.id == self.context['latest_resume']
