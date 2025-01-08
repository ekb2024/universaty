from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def  func_platform(request):
   return  render(request,"platform.html")
def  func_games(request):
      context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]}
      return  render(request,"games.html",context)

def  func_cart(request):
     return  render(request,"cart.html")
