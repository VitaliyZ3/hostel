from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.db.models import fields
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Cleaner, TypeOfNumber, Room, Order
from django import forms
from .forms import OrderForm, UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User

class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'hostelrent/login.html'

def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'hostelrent/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'hostelrent/register.html', {'user_form': user_form})

class RoomListView(generic.ListView):
    model = Room
    fields = '__all__'
    success_url = '/'


def order_create(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.visitor = request.user
            a = new_post.date_of_daparture - new_post.start_date   
            new_post.total_cost = (a.days+1)*new_post.room.rent_pay
            if print(str(Order.objects.filter(start_date__lte= new_post.start_date, date_of_daparture__gte=new_post.start_date))) != '<QuerySet []>' :
                print("СОВПАДЕНИЕ")
            if print(str(Order.objects.filter(start_date__gte= new_post.date_of_daparture, date_of_daparture__lte=new_post.date_of_daparture))) != '<QuerySet []>':
                print("СОВПАДЕНИЕ")
            new_post.save()
            return redirect('totalcost')
    return render(request, 'hostelrent/order_form.html', {'form' : form})

def total_cost(request):
    cost = Order.objects.latest('total_cost').total_cost
    print(cost)
    return render(request, 'hostelrent/showcost.html', context= {'cost' : cost})

def user_profile(request, username):
    user = User.objects.get(username=username)
    orders = Order.objects.filter( visitor = user)
    print(orders)
    context = {
       "user": user, 
       "orders" : orders
    }


    return render(request, 'hostelrent/user_profile.html', context)