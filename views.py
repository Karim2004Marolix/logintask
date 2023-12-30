from django.shortcuts import render,redirect,HttpResponse
from .models import Signup

# Create your views here.
def Registration(request):
    if request.method == 'POST':
        efirst_name = request.POST["first_name"]
        elast_name = request.POST["last_name"]
        eemail = request.POST["email"]
        eusername = request.POST["username"]
        epassword = request.POST["password"]
        econfirm_password= request.POST["confirm_password"]

        if epassword!=econfirm_password:
            return HttpResponse("Invalid Confirm Password")
        else:
            user_detals=Signup(first_name = efirst_name, last_name = elast_name,email = eemail, username = eusername, password = epassword, confirm_password = econfirm_password)
            user_detals.save()
            return redirect(login)
    return render(request,'index.html') 
        
def login(request):
    if request.method == 'POST':
        eusername = request.POST["username"]
        epassword = request.POST["password"]
        user = Signup.objects.all()
        for i in user:
            if i.username == eusername and i.password == epassword:
                return redirect(home)             
    return render(request,'login.html')

def home(request):
    if request.method == 'POST':
        return redirect(login)
    return render(request,'homepage.html')



