from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from .forms import ApplicationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['pw'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User.objects.create(
        first = request.POST['first'],
        last= request.POST['last'],
        email= request.POST['email'],
        password= pw_hash
        )
    request.session['user_id'] = new_user.id
    messages.success(request, 'Thats it!')
    return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        print(user)
        if bcrypt.checkpw(request.POST['pw'].encode("utf-8"), user.password.encode("utf-8")):
            request.session['user_id'] = user.id
            return redirect('/dashboard')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user,
        'all_applications': Application.objects.all()
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def application(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        newform.save()
    context= {
        'form': form
            }

    return render(request, 'newApplication.html', context)

def addApplication(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        Application.objects.create(
            position= request.POST['position'],
            company=request.POST['company'],
            location=request.POST['location'],
            url=request.POST['url'],
            posted_by= logged_in_user,
        )
    return redirect('/dashboard')

def viewApplication(request, num):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    form = ApplicationForm(request.POST or None)
    item = Application.objects.get(id=num)
    context ={
        'form': form,
        'logged_in_user': logged_in_user,
        'item': item,
    }
    return render(request, 'viewApplication.html', context)

def updateApplication(request, num):
    to_update = Application.objects.get(id=num)
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        to_update.position = request.POST['position']
        to_update.company = request.POST['company']
        to_update.location = request.POST['location']
        to_update.url= request.POST['url']
        to_update.save()
    return redirect('/dashboard')

def deleteApplication(request, num):
    to_delete = Application.objects.get(id=num)
    to_delete.delete()
    return redirect('/dashboard')



def user(request, num):
    view_user = User.objects.get(id=num)
    context ={
        'view_user': view_user,
        'all_applications': Application.objects.all()
    }
    return render(request, 'user.html', context)