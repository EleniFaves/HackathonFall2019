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

def getDate():

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

class DayVideos(generic.ListView):
    model = Video
    template_name = "video_stats/index.html"

    def get(self, request, *args, **kwargs):
        print('PRINT', request.GET.get('year'))

        year, month, day = getDate()

        context = {'videos' : Video.objects.filter(date=datetime.date(year, month, day)).order_by('-views'), 'date' : datetime.date(year, month, day)}
        return render(request, self.template_name, context)

class VideosByCategory(generic.DetailView):
    model = Video
    template_name = "videos_by_category/index.html"

    def get(self, request, *args, **kwargs):

        year, month, day = getDate()
        context = {
            'categories' : list(Video.objects.filter(date=datetime.date(year, month, day)).values('category_id').annotate(avgViews=Avg('views'), avgLikes=Avg('likes'), avgDislikes=Avg('dislikes'), avgCommentCount=Avg('comment_count')).order_by('avgViews').values_list('category_id', 'avgViews')),
            'idToCategory': {
                "1": "Film & Animation",
                "2": "Autos & Vehicles",
                "10": "Music",
                "15": "Pets & Animals",
                "17": "Sports",
                "18": "Short Movies",
                "19": "Travel & Events",
                "20": "Gaming",
                "21": "Videoblogging",
                "22": "People & Blogs",
                "23": "Comedy",
                "24": "Entertainment",
                "25": "News & Politics",
                "26": "Howto & Style",
                "27": "Education",
                "28": "Science & Technology",
                "30": "Movies",
                "31": "Anime/Animation",
                "32": "Action/Adventure",
                "33": "Classics",
                "34": "Comedy",
                "35": "Documentary",
                "36": "Drama",
                "37": "Family",
                "38": "Foreign",
                "39": "Horror",
                "40": "Sci-Fi/Fantasy",
                "41": "Thriller",
                "42": "Shorts",
                "43": "Shows",
                "44": "Trailers"
            },
            'date' : datetime.date(year, month, day)
        }
        return render(request, self.template_name, context)