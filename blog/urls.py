#! /usr/bin/env python
# -*- coding:utf-8 -*-
# data:2018/2/6
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    url(r'^(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]