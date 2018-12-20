#! /usr/bin/env python
# -*- coding:utf-8 -*-
# data:2018/2/7
from django import forms
# 导入Djagno默认的用户模型User类
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# 一般情况下，如果提交表单后，不会对数据库进行修改，则继承 Form 类。
# 如果要将表单类中的数据写入到数据表或者某些记录的值，就要让表单继承 ModelForm 类
# 注册用户的表单类
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    # 声明表单类所应用的数据模型，也就是将来表单的内容会写入到哪个数据库中的哪些记录里面。
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do match.")

        return cd['password2']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("phone", "birth")

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)