from django.shortcuts import render
from .forms import UserRegistrationForm
def home(request):
    name='Manasa'
   
    numbers=[1,2,3,4,5,6,7,8,9]
    context={'name':name,'numbers':numbers}
    return render(request, 'myapp/home.html', context)
   
def login(request):
    return render(request, 'myapp/login.html')

def register(request):
    form=UserRegistrationForm()
    context={'form':form}
    return render(request, 'myapp/register.html',context)