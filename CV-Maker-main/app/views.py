from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from .models import Student
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'app/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                messages.success(request,'Registered Successfully!!!')
                fm.save()
                fm = SignupForm()
                return HttpResponseRedirect('/login/')
        else:
            fm = SignupForm()
        return render(request, 'app/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully!!!')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')


def preview(request):
    if request.user.is_authenticated:
        details = Student.objects.filter(user=request.user)
        if(details):
            data = details[0]
        else:
            data = {}
        return render(request, 'app/preview.html',{'data':data})
    else:
        return HttpResponseRedirect('/login/')

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            student_details = Student.objects.filter(user=request.user)
            if(student_details):
                student_details = student_details[0]
                student_details.email = request.POST.get('email')
                student_details.fullname = request.POST.get('fullname')
                student_details.dob = request.POST.get('dob')
                student_details.adress = request.POST.get('adress')
                student_details.clgname = request.POST.get('clgname')
                student_details.clgyear = request.POST.get('clgyear')
                student_details.clgyear = request.POST.get('clgyear')
                student_details.clgcpi = request.POST.get('clgcpi')
                student_details.cls12name = request.POST.get('cls12name')
                student_details.cls12year = request.POST.get('cls12year')
                student_details.cls12cpi = request.POST.get('cls12cpi')
                student_details.cls10name = request.POST.get('cls10name')
                student_details.cls10year = request.POST.get('cls10year')
                student_details.cls10cpi = request.POST.get('cls10cpi')
                student_details.intrest = request.POST.get('intrest')
                student_details.planguages = request.POST.get('planguages')
                student_details.toolsandtech = request.POST.get('toolsandtech')
                student_details.projectname = request.POST.get('projectname')
                student_details.projectguide = request.POST.get('projectguide')
                student_details.projectdesc = request.POST.get('projectdesc')
                student_details.hobby1 = request.POST.get('hobby1')
                student_details.hobby2 = request.POST.get('hobby2')
                student_details.hobby3 = request.POST.get('hobby3')
                student_details.hobby4 = request.POST.get('hobby4')
                student_details.save()
            else:
                fullname = request.POST.get('fullname')
                email = request.POST.get('email')
                dob = request.POST.get('dob')
                adress = request.POST.get('adress')
                clgname = request.POST.get('clgname')
                clgyear = request.POST.get('clgyear')
                clgyear = request.POST.get('clgyear')
                clgcpi = request.POST.get('clgcpi')
                cls12name = request.POST.get('cls12name')
                cls12year = request.POST.get('cls12year')
                cls12cpi = request.POST.get('cls12cpi')
                cls10name = request.POST.get('cls10name')
                cls10year = request.POST.get('cls10year')
                cls10cpi = request.POST.get('cls10cpi')
                intrest = request.POST.get('intrest')
                planguages = request.POST.get('planguages')
                toolsandtech = request.POST.get('toolsandtech')
                projectname = request.POST.get('projectname')
                projectguide = request.POST.get('projectguide')
                projectdesc = request.POST.get('projectdesc')
                hobby1 = request.POST.get('hobby1')
                hobby2 = request.POST.get('hobby2')
                hobby3 = request.POST.get('hobby3')
                hobby4 = request.POST.get('hobby4')
                
                data = Student(user=request.user,fullname=fullname,email=email, dob=dob, adress=adress, clgname=clgname, clgyear=clgyear, clgcpi=clgcpi, cls12name=cls12name, cls12year=cls12year, cls12cpi=cls12cpi, cls10name=cls10name, cls10year=cls10year, cls10cpi=cls10cpi, intrest=intrest, planguages=planguages, toolsandtech=toolsandtech, projectname=projectname, projectguide=projectguide, projectdesc=projectdesc, hobby1=hobby1, hobby2=hobby2, hobby3=hobby3,hobby4=hobby4)

                data.save()
            messages.success(request, 'Saved Successfully!!!')
            return HttpResponseRedirect('/preview/')
        
        details = Student.objects.filter(user=request.user)
        if(details):
            data = details[0]
        else:
            data={}
        return render(request, 'app/dashboard.html',{'data':data})
    else:
        return HttpResponseRedirect('/login/')