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

    def getDate(self):

        year = random.randint(2017,2018)

        if year == 2017:
            month = random.randint(11,12)
            if month == 12:
                day = random.randint(1,31)
            else:
                day = random.randint(14,30)
        else:
            month = random.randint(1,6)
            if month == 4:
                day = random.randint(1,30)
            elif month == 6:
                day = random.randint(1,14)
            elif month == 2:
                day = random.randint(1,28)
            else:
                day = random.randint(1,31)

        return year, month, day

    def get(self, request, *args, **kwargs):
        print('PRINT', request.GET.get('year'))

        year, month, day = self.getDate()

        context = {'videos' : Video.objects.filter(date=datetime.date(year, month, day)), 'date' : datetime.date(year, month, day)}
        return render(request, self.template_name, context)

class VideosByCategory(generic.DetailView):
    model = Video
    template_name = "videos_by_category/index.html"

    def get(self, request, *args, **kwargs):
        context = {'categories' : Video.objects.values('category_id').annotate(avgViews=Avg('views'), avgLikes=Avg('likes'), avgDislikes=Avg('dislikes'), avgCommentCount=Avg('comment_count'))}
        return render(request, self.template_name, context)