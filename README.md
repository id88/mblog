
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

包含的应用：
 - blog
 - account
 - register

### 简单的博客

#### 在后台添加博客

#### 博客列表

#### 博客内容展示


### 用户的登录和退出
使用django内置的方法登录和退出

### 用户注册
普通用户注册

### 修改密码


### 重置密码
（这个功能还没完全实现，待后期完善...）

### 展示个人信息
查看用户注册时填写的个人信息

### 编辑个人信息
修改个人信息

### 上传用户头像
上传头像时可对头像进行裁剪

### 对普通用户进行管理
管理员可删除和添加普通用户，也可对普通用户的信息进行修改

---





