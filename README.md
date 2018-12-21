
## 简介

一个博客系统


## 运行环境：

- Python 3.6
- Django版本：1.11


 0、安装依赖的模块
```
pip install -r requirements.txt
```

 1、创建数据库
（本项目使用 sqlite3 数据库）
```
python manage.py makemigrations

python manage.py migrate
```

 2、创建超级管理员
```
python manage.py createsuperuser
```
然后输入用户名、Email和密码

 3、运行项目
```
python manage.py runserver
```
浏览器访问：http://127.0.0.1:8000/admin/
输入第2步创建的管理员账户及密码



## 功能
