from django.urls import path

from myweather import views

urlpatterns = [
    # show what temp function returns
    path("myweather/", views.temp_current, name='temp_current'),
    path("myweather/discover", views.temp_somewhere, name='temp_somewhere')

]
