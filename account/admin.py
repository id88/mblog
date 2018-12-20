#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import UserProfile
from .models import UserInfo

class UserProfileAdmin(admin.ModelAdmin):
    # 列出列表中的项目
    list_display = ('user', 'birth', 'phone')
    # 规定网页右边的 FILTER 的显示内容，通过过滤电话号码显示的列表内容
    list_filter = ("phone",)  #注意逗号

admin.site.register(UserProfile, UserProfileAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'profession', 'address', 'aboutme', 'photo')
    list_filter = ("school", "company", "profession")

admin.site.register(UserInfo, UserInfoAdmin)
