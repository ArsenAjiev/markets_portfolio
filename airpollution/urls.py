from django.urls import path
from airpollution.views import airpollution, temp_country_creator, temp_add_colors_to_pollutants

app_name = 'airpollution'

urlpatterns = [
    path('', airpollution, name='airpollution'),
    path('temp_country_creator/', temp_country_creator, name='temp_country_creator'),
    path('temp_add_colors_to_pollutants/', temp_add_colors_to_pollutants, name='temp_add_colors_to_pollutants'),

]
