from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.utils import timezone
from django.contrib import messages
from django.db.models.query import QuerySet
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name',False)
        last_name = request.POST.get('last_name',False)
        username = request.POST.get('username',False)
        email = request.POST.get('email',False)
        psw1 = request.POST.get('psw1',False)
        psw2 = request.POST.get('psw2',False)
        
        if psw1==psw2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user( first_name=first_name,last_name=last_name,username=username ,  email=email,password=psw1 )
                user.last_login = timezone.now()
                user.save()
                print('user created')
                return redirect("/")
        else:
            print("password not matching")
            return redirect('signup')
        return redirect("/")
    else:
        return render(request,'signup.html')
# Create your views here
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            messages.info(request,'logged in')
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def main(request):
    return render (request,'main.html')
def home(request):
    return render(request, 'home.html')
def guideline(request):
    return render(request, 'guideline.html')
def afterlogin(request):
    post = suggestion.objects.all()
    logged_in_user_posts = suggestion.objects.filter(user=request.user)
    context={'post':post,'logged_in_user_posts':logged_in_user_posts}
    return render(request,'index.html',context)
def logout(request):
    return render(request,'home.html')
def profile(request):
    post = suggestion.objects.all()
    logged_in_user_posts = suggestion.objects.filter(user=request.user)
    context={'post':post,'logged_in_user_posts':logged_in_user_posts}
    return render(request,'profile.html',context)

from django.shortcuts import render
from .forms import sugg_form
from .models import suggestion
from django.conf import settings

def suggestpage(request):
    if request.method == 'POST':
        form=sugg_form(request.POST)
        if form.is_valid():
            suggest=request.POST.get('suggest',False)
            title=request.POST.get('title',False)
            obj=suggestion(text=suggest,title=title)
            obj.user=request.user
            obj.save()
            return redirect('index.html')
        else:
            form=sugg_form()
    else:
        return render(request,'suggestpage.html')
    