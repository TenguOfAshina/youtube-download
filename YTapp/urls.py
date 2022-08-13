#from django.contrib import admin
from django.urls import path
from YTapp import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('admin/', admin.site.urls),
    path('download/', views.download_video, name='download'),
]