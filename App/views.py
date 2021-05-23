from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from App.custom import model_dict, cart_count
from django.views.decorators.csrf import csrf_exempt

from.models import *

# Create your views here.


def home(request):
	return render(request, 'index.html')


# ************************************************************* Register new user *******************************************************

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'message': None})
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            new_user = User.objects.create_user(username, email, password,
                                                first_name=first_name.title(),
                                                last_name=last_name.title())
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home')) 
        else:
            return render(request, 'register.html', {'message': 'User already exists.'})

# ******************************************************************** Login page ***********************************************************

def login_view(request):
	if request.user.is_authenticated:
	    return HttpResponseRedirect(reverse('home'))

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
		    login(request, user)
		    return HttpResponseRedirect(reverse('home'))
		else:
		    return render(request, 'login.html', {'message': 'Invalid credentials'})
	return render(request, "login.html", {"message" : None})

# **************************************************************** Log out user **************************************************************

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# **************************************************************** All Orders **************************************************************

def orders_view(request ):
	if request.user.is_authenticated:
		pizza = Pizza.objects.all()
		orders = Order.objects.filter(user = request.user)
		context = {'pizza' : pizza, 'orders' : orders}
		return render(request , 'orders.html', context)
	return HttpResponseRedirect(reverse('login'))

# **************************************************************** Order user **************************************************************

def order_view(request , order_id):
    order = Order.objects.filter(order_id=order_id).first()
    if order is None:
        return HttpResponseRedirect('/')
    
    context = {'order' : order}
    return render(request , 'order.html', context)

@csrf_exempt
def order_pizza(request):
    user = request.user
    data = json.loads(request.body)
    
    try:
        pizza =  Pizza.objects.get(id=data.get('id'))
        order = Order(user=user, pizza=pizza , amount = pizza.price)
        order.save()
        return JsonResponse({'message': 'Success'})
        
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Something went wrong'})