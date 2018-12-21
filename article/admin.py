from django.contrib import admin
from .models import ArticleColumn

# 使得管理员也能对文件栏目编辑和删除

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ("column", "created", "user")
    list_filter = ("column",)

admin.site.register(ArticleColumn, ArticleColumnAdmin)