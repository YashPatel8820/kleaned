from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from USER.models import *
from django.contrib import messages

# Create your views here.

def hello(request):
    return HttpResponse('hii Yash')

# def login_page(request):
#     return render(request, 'USER/loginnew.html')

# def register_page(request):
#     return render(request, 'USER/Register.html')


# =====================\\For user Registration//==================    

def register_page(request):
    if request.POST:
        n = request.POST['name']
        print('n')
        e = request.POST['email']
        print('e')
        p = request.POST['password']
        print('p')
        cp = request.POST['cpassword']
        print('cp')

        try:
            if cp == p:
                v = Registration()
                v.Name = n
                v.Email = e
                v.Password = p
                v.save()
                return redirect('Login')
            else:
                w = "Please Confirm Your Password"
                return render(request, 'USER/Register.html', {'warning' : w})
        finally:
            messages.success(request, 'Form successfully submitted')
    
    return render(request, 'USER/Register.html')

# =====================\\For user Registration//==================   

def login_page(request):
    if request.POST:
        n = request.POST.get('name')
        print(n)
        p = request.POST.get('password')
        print(p)
        try:
            check = Registration.objects.get(Name=n)
            print(check) 
            if check.Password==p:
                request.session['name'] = check.Name
                return redirect('Home')
                # return render(request, 'HOME/index.html', {'Head' : check})
            else:
                war1 = "Enter Correct Password"
                print(war1)
                return render(request, 'USER/loginnew.html', {'warning1' : war1})
        except:
            war2 = "Enter Correct UserName"
            return render(request, 'USER/loginnew.html', {'warning2' : war2})

    return render(request, 'USER/loginnew.html')
                            

def logout_page(request):
    if 'name' in request.session.keys():
        
        del request.session['name']
        return redirect('Home')    
    else:
        return redirect('Login')   
               