from django.shortcuts import render
from .models import *
# from django.shortcuts import render
# from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    # Your view logic here
    return render(request, 'home.html')

def HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 

def index(request):
    return render(request,'index.html')

def regView(request):
    return render (request,'reg.html')

def regData(request):
    if request.method=='POST':
        uname = request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        newdata=student.objects.filter(Email=email)
        if newdata:
            message='User already registered'
            return render(request,'reg.html',{'msg':message})
        else:
            if password == cpassword:
                ndata=student.objects.create(Username=uname,Email=email,Password=password)
                message='User Successfully Register'
                return render(request,'login.html',{'msg':message})
            else:
                message="Password doesn't match"
                return render(request,'reg.html',{'msg':message})
            
def loginView(request):
    return render(request,'login.html')


def loginData(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        ldata=student.objects.get(Email=email)
        if ldata:
            request.session['Username']=ldata.Username
            if ldata.Password==password:
                return render(request,'chatbot_homePage.html')
            else:
                message='Password or Username mismatch'
                return render(request,'login.html',{'msg':message})
            
        

def chatbotView(request):
    return render (request,'chatbot_homePage.html')

def faqView(request):
    return render(request,'faq.html')
def aboutView(request):
    return render(request,'about.html')

def textView(request):
    return render(request,'text.html')