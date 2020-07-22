from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html',{'password': 'Akjsaçldfkj83'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvwyz')
    the_password = ''
    length = int(request.GET.get('length'), 12)

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZ'))

    if request.GET.get('special'):
        characters.extend("!#$%&'()*+,-./:;<=>?@[]^_`{|}~")

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    for x in range(0,length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html',{'password' : the_password})


def about(request):
    return render(request, 'generator/about.html')