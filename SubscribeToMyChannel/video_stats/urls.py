from django.urls import path
from . import views
urlpatterns = [
    path('', views.DayVideos.as_view()),
    path('categorical/', views.VideosByCategory.as_view())
]