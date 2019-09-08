# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Video
import datetime

class video_stats(generic.ListView):
    model = Video
    template_name = "video_stats/index.html"

    def get(self, request, *args, **kwargs):
        context = {'videos' : Video.objects.filter(date=datetime.date(2018, 1, 1))}
        return render(request, self.template_name, context)