#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import UserProfileForm, UserInfoForm, UserForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("You have been authenticated successfully")
            else:
                return HttpResponse("Username or password incorrect")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})
        # return render(request, "account/login2.html", {"form": login_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid()*userprofile_form.is_valid():
            # ModelForm 类或其子类都具有 save()方法，作用是将数据保存到数据库中，并生成该数据对象。
            # 若有参数为 commit=Fasle 则数据不保存到数据库，仅生成数据对象。
            new_user = user_form.save(commit=False)
            # 设置数据对象的密码（已经过验校），
            # 得益于前面commit=Fasle的设置，否则数据写到数据库中再设置密码就要重新写入了
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)

            return HttpResponse("successfully")

        else:
            return HttpResponse("Please check that the information is correct！")

    else:
        user_form = RegistrationForm()  # forms.py中的类
        userprofile_form = UserProfileForm()  # forms.py中的类

        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


# 展示个人信息的视图函数
@login_required(login_url='/account/login')  # 将没有登录的用户转到登录界面
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    return render(request, "account/myself.html", {"user":user, "userinfo":userinfo, "userprofile":userprofile})


# 编辑个人信息的视图函数
@login_required(login_url='/account/login/')  # 将没有登录的用户转到登录界面
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)

        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data

            print(user_cd["email"])

            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']

            user.save()
            userprofile.save()
            userinfo.save()

        # 当用户提交了个人信息被后台程序验证通过和保存后，跳转到登录界面
        return HttpResponseRedirect('/account/my-information/')

    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth":userprofile.birth, "phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school, "company":userinfo.company, "profession":userinfo.profession, "address":userinfo.address, "aboutme":userinfo.aboutme})

        return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form, "userinfo_form":userinfo_form})


# 头像裁剪的
@login_required(login_url='/account/login/')  # 将没有登录的用户转到登录界面
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)