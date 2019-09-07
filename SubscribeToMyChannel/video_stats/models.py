from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.TextField()
    date = models.DateField()
    title = models.TextField()
    category_id = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
