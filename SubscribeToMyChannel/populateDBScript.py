import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SubscribeToMyChannel.settings")
import django
django.setup()
from video_stats.models import Video

with open('../CAvideos.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        lstStr = row['trending_date'].split('.')
        dateStr = '20' + lstStr[0] + '-' + lstStr[2] + '-' + lstStr[1]
        video = Video(video_id=row['video_id'], date=dateStr, title=row['title'], category_id=row['category_id'], views=row['views'], likes=row['likes'], dislikes=row['dislikes'], comment_count=row['comment_count'])
        video.save()

csvFile.close()