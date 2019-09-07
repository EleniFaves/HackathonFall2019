# Register your models here.
from __future__ import unicode_literals
from django.contrib import admin
from .models import Video
class VideoAdmin(admin.ModelAdmin):
 model = Video

admin.site.register(Video, VideoAdmin)