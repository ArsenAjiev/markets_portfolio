from django.urls import path
from airpollution.views import airpollution, temp_country_creator

app_name = 'airpollution'

urlpatterns = [
    path('', airpollution, name='airpollution'),
    path('temp_country_creator/', temp_country_creator, name='temp_country_creator')

]
