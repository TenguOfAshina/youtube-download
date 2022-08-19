#from django.contrib import admin
from django.urls import path
from YTapp import views
from .views import HomePageView, AboutPageView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    #path('admin/', admin.site.urls),
    path('download/', views.download_video, name='download'),
]