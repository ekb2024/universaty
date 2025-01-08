from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def  func_platform(request):
    title= "Сайтик"
    text= "Главная страница"
    name_games= "Магазин"
    http_games= "http://127.0.0.1:8000/platform/games"
    name_cart = "Корзина"
    http_cart = "http://127.0.0.1:8000/platform/cart"
    context =  { 'title': title,'text':text,'name_games':name_games,'http_games':http_games,
                 'name_cart': name_cart, 'http_cart': http_cart }
    return  render(request,"platform.html",context)
def  func_games(request):
    title = "Магазин"
    text= "Игры"
    name_games1= "Atomic Heart"
    name_games2= "CyberPunk"
    name_games3= "PayDay"
    name_button = "домой"
    http_platform = "http://127.0.0.1:8000/platform/"
    context = {'title': title, 'text': text,'name_games1':name_games1,
               'name_games2':name_games2,'name_games3':name_games3 ,'name_button':name_button,'http_platform':http_platform}

    return  render(request,"games.html",context)
def  func_cart(request):
    title = "Корзина"
    text = "Ваша корзина пуста"
    name_button = "домой"
    http_platform = "http://127.0.0.1:8000/platform/"
    context = {'title': title, 'text': text,'name_button':name_button,'http_platform':http_platform}
    return  render(request,"cart.html",context)