from django.urls import path
from airpollution.views import welcome, upload_file

app_name = 'airpollution'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('upload_file/', upload_file, name='upload_file')

]
