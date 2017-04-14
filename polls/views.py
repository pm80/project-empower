from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


from polls.models import  Data

def login_page(request):   
    return render(request,'polls/login_page.html',context={})
    
def check(request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user:
        if user.is_active :
            login(request, user)
            return HttpResponseRedirect(reverse('polls:moreInfo'))
        else :
            HttpResponse('you are not active !')
    return HttpResponse('incorrect username or password !' )


def moreInfo(request):
    if request.user.is_authenticated:
        return render(request, 'polls/moreInfo.html', context={})
    return HttpResponse('user is not authenticated !')
    
def moreInfoUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'post':
            Data.objects.create(user = request.user, pin = request.POST['pin'], address = request.POST['address'])
            HttpResponseRedirect(reverse('polls:database'))
        else: return HttpResponseRedirect(reverse('polls:database'))
    return HttpResponseRedirect(reverse('polls:database'))

def database(request):
    return HttpResponse('page creation is in progress !')

def signup(request):
    context = {}
    return render(request, 'polls/signup.html', context)
def signup_fun(request):
    
    if request.POST['password'] != request.POST['confirm_password']:
        return HttpResponse('password does not match')
    else:
        User.objects.create_user(username=request.POST['email'], email=request.POST['email'], password=request.POST['password'])



        return HttpResponseRedirect(reverse('polls:login_page'))
