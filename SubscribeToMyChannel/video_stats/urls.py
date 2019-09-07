from django.urls import path
from . import views
urlpatterns = [
    path('', views.Video.as_view()),
]