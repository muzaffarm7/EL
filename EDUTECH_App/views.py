from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import dj_static

# Create your views here.

def About(request):
	return render(request,'about.html')

def Contact(request):
	return render(request,'contact.html')

def Index(request):
	if not request.user.is_staff:
		return redirect('login')
	return render(request,'index.html')		

def LogIn(request):
	error = ""
	if request.method=='POST':
		u = request.POST['uname']
		p = request.POST['pwd']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error="no"
			else:
				error="yes"
		except:
			error = "yes"	
	d = {'error':error}			
	return render(request,'login.html',d)

def Logout_Admin(request):
	if not request.user.is_staff:
		return redirect('login')
	logout(request)	
	return redirect('login')		 	
		
def View_Student(request):
    if not request.user.is_staff:
        return redirect('login')
    stud = Student.objects.all()
    d = {"stud":stud}
    return render(request,'view_student.html',d)	

def Add_Student(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        ag = request.POST['age']
        c = request.POST['mobile']
        ad = request.POST['address']
        em = request.POST['email']
        try:
            Student.objects.create(name=n, gender=g,mobile=c,address=ad,age=ag,emailid=em)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_student.html',d)

def Delete_Student(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	student = Student.objects.get(id=pid)
	student.delete()
	return redirect('view_student') 
