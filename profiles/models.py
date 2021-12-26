from django.db import models
from .utils import resume_update_path

class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return self.name
    
    @property
    def latest_resume(self):
        return self.resume_set.order_by('created_at').last()


class Resume(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    file = models.FileField(upload_to=resume_update_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Resume for {} (resume id: {})".format(self.profile.name, self.id)
