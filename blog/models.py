#-*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
	#规定字段title的属性为CharField(),并以max_length=50的形式说明字段的最大数量
	# 标题　字符串类型　　最大长度200
    title = models.CharField(max_length=200)

	#类User是BlogArticles对应对象，related_name="blog_posts"的作用是允许通过类User反向查找到BlogArticles
	# 作者 一对多设计　多方持有一方的外键
	# 千万不能少了写 on_delete=models.CASCADE 这是个坑
    author = models.ForeignKey(User, related_name="blog_posts",on_delete=models.CASCADE)

	# 内容 文本类型
    body = models.TextField()

	# 发布时间 时间类型
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)#注意逗号

    def __str__(self):
        return self.title

