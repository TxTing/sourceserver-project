from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'account/signup.html', {'error':'Password must be same'})
    else:
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('userpage')
        else:
            return render(request, 'account/login.html', {'error':'Incorrect account or password!'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
