from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from random import randint
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from .models import User

# Create your views here.

def generate_code():
    return randint(100000,999999)

class UserRegistrarionView(View):
    form_class = UserRegistrationForm
    def get(self, request):
        form = self.form_class()
        context = {
            "form": form
        }
        return render(request, 'accounts/signup.html', context)
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)
        
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered")
            return redirect('accounts:login')
        context = {
            "form": form
        }
        return render(request, 'accounts/signup.html', context)
   
class UserLoginView(View):
    form_class = UserLoginForm
    def get(self,request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)
        context = {
            "form": form
        } 
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                messages.success(request, "You have logged in")
                login(request,user)
                return redirect("index")
            messages.error(request, "Username not found")
            return render(request, "accounts/login.html", context) 
            
        messages.error(request, "Something went wrong")
        return render(request, "accounts/login.html", context)
            
class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request, "You have logged out")
        return redirect("index")
    

class UserUpdateView(View):
    form_class = UserUpdateForm
    
    def get(self, request):
        form = self.form_class()
        context = {
            "form": form
        }
        return render(request, "accounts/userupdate.html", context)

    def post(self,request):
       
        user = request.user
        data = request.POST
        files = request.FILES
        
        form = self.form_class(data=data, files=files, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect("index")
        
        context = {
            "form": form
        }
       
        messages.error(request, "Something went wrong")
        return render(request, "accounts/userupdate.html", context)


class ResetPasswordView(View):
    
    def get(self, request):
        return render(request, 'accounts/resetpassword.html')
    
    def post(self, request):
        code = str(generate_code())
        print(code, '==============================================')
        username = request.POST.get("username")
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            user.set_password(code)
            user.save()
            
            #password sent user's email or number 
            messages.success(request, "Password changed successfully, new password sent your email")
            return redirect("accounts:login")
        
        messages.error(request, "Username not found")
        return render(request, 'accounts/resetpassword.html')
        
