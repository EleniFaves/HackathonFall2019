# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from django.db.models import Avg
from .models import Video
import datetime
import random


class DayVideos(generic.ListView):
    model = Video
    template_name = "video_stats/index.html"

    def get(self, request, *args, **kwargs):
        print('PRINT', request.GET.get('year'))
        context = {'videos' : Video.objects.filter(date=datetime.date(2018, 1, 1))}
        return render(request, self.template_name, context)

class VideosByCategory(generic.DetailView):
    model = Video
    template_name = "videos_by_category/index.html"

    def get(self, request, *args, **kwargs):
        context = {'categories' : Video.objects.values('category_id').annotate(avgViews=Avg('views'), avgLikes=Avg('likes'), avgDislikes=Avg('dislikes'), avgCommentCount=Avg('comment_count'))}
        return render(request, self.template_name, context)