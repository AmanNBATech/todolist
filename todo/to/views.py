from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def sign(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        pass4=request.POST['pass1']
        pass5=request.POST['pass2']
 
        if pass4==pass5:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username already exists')
                return redirect('sign')
            
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email already exists')
                return redirect('sign')
            else:
                User.objects.create_user(username=username,email=email,password=pass5)
                messages.success(request,'Account Has Been Created')
                return redirect('login')
        else:
            return redirect('sign')
        

def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    else:
        username=request.POST['username']
        password=request.POST['pass1']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'invalid userame or password')
            return redirect('login')


@login_required(login_url='login')
def index(request):
    if request.method=='GET':
     if request.user.is_authenticated:
         user =request.user
         print(user)
         info=todo.objects.filter(use=user)
         return render(request,'index.html',{'info':info})
     else:
         return redirect('login')

         
     
     
    
    else:
        task=request.POST['task']
        task_date=request.POST['task_date']

        info=todo(task=task,task_date=task_date,use=request.user)
        info.save()
        return redirect('home')
def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    user =request.user
    print(user)
    info=todo.objects.filter(use=user)
    

    return render(request,'home.html',{'info':info})

def update(request,id):
    if request.method=='GET':
      user =request.user
      print(user)
      info=todo.objects.filter(use=user)
      inform = todo.objects.get(id=id)  
      return render(request,'index.html',{'info':info,'inform':inform})
    
    else:
      task=request.POST['task']
      task_date=request.POST['task_date']
      info=todo(id=id,task=task,task_date=task_date,use=request.user)
      info.save()
      return redirect('home')
    
def delete(request,id):
     info=todo.objects.get(id=id)
     info.delete()
     return redirect('home')