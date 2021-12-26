from django.contrib import admin
from .models import Profile, Resume

admin.site.register([Profile, Resume])
