#! /usr/bin/env python
# -*- coding:utf-8 -*-
# data:2018/2/7
from django.conf.urls import url
from . import views
from django.conf import settings

# 引入Django内置的视图函数，并将其重名名为auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 调用views.py 中的 user_login 函数
    # url(r'^login/$', views.user_login, name="user_login"),

    # 使用Django内置的登录
    url(r'^login/$', auth_views.login, name="user_login"),

    # 使用Django内置的登录，但使用自己编写的登录模板文件
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}),

    # 使用Django内置的退出
    # url(r'^logout/$', auth_views.logout, name="user_logout"),

    # 使用Django内置的退出，但使用自己编写的退出模板文件
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name="user_logout"),

    # 用户注册
    url(r'^register/$', views.register, name="user_register"),


    # 内置的修改密码
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect": "/account/password-change-done"}, name="password_change"),
    url(r'^password-change-done/$', auth_views.password_change_done, name="password_change_done"),

    # 第三方重置密码
    url(r'^password-reset/$', auth_views.password_reset, {"template_name":"account/password_reset_form.html", "email_template_name":"account/password_reset_email.html", "post_reset_redirect":"/account/password-reset-done"}, name="password_reset"),
    url(r'^password-reset-done/$', auth_views.password_reset_done, {"template_name":"account/password_reset_done.html"}, name="password_reset_done"),
	url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, {"template_name":"account/password_reset_confirm.html", "post_reset_redirect":"/account/password-reset-complete"}, name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete, {"template_name":"account/password_reset_complete.html"}, name="password_reset_complete"),

    # 展示个人信息
    url(r'^my-information/$', views.myself, name="my_information"),

    # 编辑个人信息
    url(r'^edit-my-information/$', views.myself_edit, name="edit_my_information"),

    # 上传和裁剪头像图片
    url(r'^my-image/$', views.my_image, name="my_image"),
]