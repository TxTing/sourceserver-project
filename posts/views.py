from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.utils import timezone

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authentaicated():
            return HttpResponse(
                'Hello there! You are acting on behalf of "%s"\n'
                % (request.user)
            )
        else:
            return HttpResponse('Hello, OAuth2!\n')

def homepage(request):
    posts = Posts.objects.all()
    return render(request, 'posts/homepage.html', {'posts':posts})

@login_required(login_url="/account/signup")
def createposts(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES.get('image', False):
            posts = Posts()
            posts.title = request.POST['title']
            posts.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                posts.url = request.POST['url']
            else:
                posts.url = 'http://' + request.POST['url']
            #posts.icon = request.FILES['icon']
            posts.image = request.FILES['image']
            posts.pub_date = timezone.datetime.now()
            posts.post_owner = request.user
            posts.save()
            return redirect('/posts/' + str(posts.id))
        else:
            return render(request, 'posts/createposts.html', {'error':'All fields are required.'})
    else:
        return render(request, 'posts/createposts.html')

def detail(request, posts_id):
    posts = get_object_or_404(Posts, pk=posts_id)
    return render(request, 'posts/detail.html', {'posts':posts})

@login_required(login_url="/account/signup")
def pushlike(request, posts_id):
    if request.method == 'POST':
        posts = get_object_or_404(Posts, pk=posts_id)
        posts.likes_total += 1
        posts.save()
        return redirect('/posts/' + str(posts.id))

@login_required(login_url="/account/signup")
def deletepost(request, posts_id):
    if request.method == 'POST':
        posts = get_object_or_404(Posts, pk=posts_id)
        posts.delete()
        return redirect('userpage')

# @login_required(login_url="/account/signup")
# def userpage(request):
#     posts = Posts.objects.all()
#     return render(request, 'posts/userpage.html', {'posts':posts})


@login_required(login_url="/account/signup")
def userpage(request):
    posts = Posts.objects.all()
    return render(request, 'posts/userpage.html', {'posts':posts})
