from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
users =['lom','istr','jem','kevi','link']
info = {}
def  sign_up_by_html(request):
     if request.method == 'POST':
        username= request.POST.get("username")
        password = request.POST.get('password')
        repeat_password= request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users and password==repeat_password and int(age) >= 18 :
            return render(request, 'registration_page.html', {'username':f'Приветствуем,{username} !'})
        else:
           if password != repeat_password : info.update({'error':'Пароли не совпадают'})
           if int(age) < 18:  info.update({'error':'Вы должны быть старше 18'})
           if username  in users: info.update({'error':'Пользователь уже существует'})
           return render(request, 'registration_page.html',info)
     return  render(request,'registration_page.html')


def  sign_up_by_django(request):
     if request.method == 'POST':
         form = UserRegister(request.POST)
         if form.is_valid():
             username = form.cleaned_data["username"]
             password = form.cleaned_data['password']
             repeat_password = form.cleaned_data['repeat_password']
             age = form.cleaned_data['age']
             if username not in users and password == repeat_password and int(age) >= 18:
                 return render(request, 'registration_page.html', {'username': f'Приветствуем,{username} !'})
             else:
                 if password != repeat_password: info.update({'error': 'Пароли не совпадают'})
                 if int(age) < 18:  info.update({'error': 'Вы должны быть старше 18'})
                 if username in users: info.update({'error': 'Пользователь уже существует'})
                 return render(request, 'registration_page.html', info)
             print("gtegttrthryh")
     else:
         form = UserRegister()
     return render(request, 'registration_page.html',{'form':form})

