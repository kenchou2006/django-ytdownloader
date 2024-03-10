from django.shortcuts import render
from .functions import get_video_info

def ytdownload(request):
    video_url = request.POST.get('video_url', '') or request.GET.get('url', '')
    if not video_url and request.method == 'POST':
        video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    if request.method == 'POST':
        video_info = get_video_info(video_url)
        return render(request, 'ytdownload.html', {'video_info': video_info, 'video_url': video_url})
    return render(request, 'ytdownload.html', {'video_url': video_url})
