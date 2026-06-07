from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('Hi World! This is the 2nd view :)')

def profile(request):
    parsed_data = []
    if request.method == 'POST':
        username = request.POST.get('user', '').strip()

        #optional auth headers
        headers = {}
        if getattr(settings, 'GITHUB_TOKEN', ''):
            headers['Authorization'] = f'token {settings.GITHUB_TOKEN}'

        response = requests.get(
            f'https://api.github.com/users/{username}',  
            headers=headers,
            timeout=5,
        )

        if response.status_code == 200:
            data = response.json()
            user_data = {
                'name':         data.get('name'),
                'blog':         data.get('blog'),
                'email':        data.get('email'),
                'public_gists': data.get('public_gists'),
                'public_repos': data.get('public_repos'),
                'avatar_url':   data.get('avatar_url'),
                'followers':    data.get('followers'),
                'following':    data.get('following'),
                'bio':          data.get('bio'),
                'location':     data.get('location'),
            }
            parsed_data.append(user_data)

    return render(request, 'app/profile.html', {'data': parsed_data})