from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import action
from .models import Profile, Resume
from .serializers import ProfileSerializer, ResumeSerializer

class ProfileView(viewsets.ModelViewSet):
    model = Profile
    queryset = model.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super(ProfileView, self).get_queryset().filter(is_deleted=False)

    @action(detail=True, methods=['post'])
    def delete_profile(self, request, pk=None):
        profile = self.get_object()
        profile.is_deleted = True
        profile.save()
        return response.Response("Profile sucessfully deleted")

    @action(detail=True, methods=['post'], serializer_class=ResumeSerializer)
    def update_resume(self, request, pk=None):
        profile = self.get_object()
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resume_file = serializer.validated_data['file']
        Resume.objects.create(profile=profile, file=resume_file)
        return response.Response("Resume updated successfully")

    @action(detail=True, methods=['get'])
    def resumes(self, request, pk=None):
        profile = self.get_object()
        latest_resume = profile.latest_resume.id
        resumes = profile.resume_set.order_by('-created_at')
        serializer = ResumeSerializer(resumes, many=True,
                                      context={'latest_resume': latest_resume})
        return response.Response(serializer.data)