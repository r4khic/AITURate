from django.shortcuts import render, redirect

from .models import User
import pymysql
from django.contrib import messages

db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     db='aituraite',
                     charset='utf8',
                     autocommit=True,
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


def base(request):
    return render(request, 'accounts/base.html', {'title': 'AITU RATE BY GUYS AND PHONK'})


def login(request):
    query = 'select * from users'
    if request.method == 'POST':
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        for result in results:
            login = result['login']
            pswrd = result['password']
            username = request.POST.get('username')
            password = request.POST.get('password')
            if login == username and pswrd == password:
                print('ok')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        user = User()
        user.f_name = request.POST.get("name")
        user.l_name = request.POST.get("surname")
        user.login = request.POST.get("login")
        user.email = request.POST.get("email")
        user.password = request.POST["password"]
        if user.f_name == '' or user.l_name == '' or user.login == '' or user.email == '' or user.email == '' or user.password == '':
            messages.info(request, 'some fields are empty')
            return redirect('register')
        query = 'INSERT INTO `users`(`name`, `surname`, `login`, `email`,`password`) VALUES (%s,%s,%s,%s,%s)'
        cursor.execute(query, (user.f_name, user.l_name, user.login, user.email, user.password))
        cursor.close()

    return render(request, 'accounts/registration.html')


def disciplines(request):
    return render(request, 'accounts/disciplines.html')


def teachers(request):
    return render(request, 'accounts/teachers.html')


def teacher(request):
    return render(request, 'accounts/teacher.html')


def rating(request):
    return render(request, 'accounts/ratings.html')