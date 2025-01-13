from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and number")
            return redirect('/')

        if password1 != password2:
            messages.error(request, "Password do not match")
            return redirect('/')
        


        # Create a user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your TRIPEDY account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")



def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/tourpackage')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('Tripedy')

    return HttpResponse('404 - Not Foud')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("Tripedy")
