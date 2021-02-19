from django.shortcuts import render,HttpResponseRedirect
from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from authForm_app.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from myApp import views
from myApp.models import Customer
#Create your views here.

# #def sign_up(request):
#         if request.method == "POST":
#             fc = UserCreationForm(request.POST)
#             if fc.is_valid():
#                 fc.save()    
#                 messages.success(request,'Sucessfully Submitted')
#         else:
#             fc = UserCreationForm()
#         return render(request,'signup.html',{'form':fc})
                
#user signup
def sign_up(request):
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                print(fm.save())
                data = Customer(user=user) 
                data.save()
                user.save()
                fm.save() 
                messages.success(request,'Sucessfully Submitted')
        else:
            fm = SignUpForm()
        return render(request,'authForm/signup.html',{'form':fm})
 
#User Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
                fm = AuthenticationForm(request=request,data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upass = fm.cleaned_data['password'] 
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request,user)
                        return HttpResponseRedirect('/userprofile/')
        else:
            fm=AuthenticationForm()
        return render(request,'authForm/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userprofile/')

#User Profile
def user_profile(request):
    if request.user.is_authenticated:
        return views.store(request)
    else:
        return HttpResponseRedirect('/userlogin/')

#User logout   
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/userlogin/')

#Change password using old password
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
                fm = PasswordChangeForm(user=request.user,data=request.POST)
                if fm.is_valid():
                    fm.save()
                    update_session_auth_hash(request,fm.user)   
                    messages.success(request,"Password Changed Sucessfully")
                    return HttpResponseRedirect('/userprofile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'authForm/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userprofile/')

#Change password without using old password
#def user_changepass(request):#
    # if request.user.is_authenticated:
    #     if request.method == "POST":
    #             fm = SetPasswordForm(user=request.user,data=request.POST)
    #             if fm.is_valid():
    #                 fm.save()
    #                 update_session_auth_hash(request,fm.user)   
    #                 messages.success(request,"Password Changed Sucessfully")
    #                 return HttpResponseRedirect('/userprofile/')
    #     else:
    #         fm = SetPasswordForm(user=request.user)
    #     return render(request,'changepass.html',{'form':fm})
    # else:
    #     return HttpResponseRedirect('/userprofile/')