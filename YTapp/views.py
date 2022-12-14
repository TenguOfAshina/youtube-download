from django.shortcuts import render, redirect
from django.http import HttpResponse
import yt_dlp
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


def home(request):
    return render(request, 'home.html')



def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_opts = {
                "format": "mp4/res:1080",
                'outtmp1': 'D:/',
                'ignoreerrors:': 'only_download',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')
    return redirect('home')
