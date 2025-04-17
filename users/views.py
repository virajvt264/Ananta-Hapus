from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, CustomerDetailsForm
from django.contrib.auth.decorators import login_required
from .models import CustomerDetails
from mango_shop.models import Orders
import json

def register(request):
    if request.method== "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account is created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})




def customer_form_view(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            # Automatically set the logged-in user
            form.instance.user = request.user
            form.save()
            return redirect('customer_list')  # Redirect to the list view
    else:
        form = CustomerDetailsForm()
    return render(request, 'users/customer_form.html', {'form': form})

def customer_list_view(request):
    user = request.user
    customers = CustomerDetails.objects.filter(user=user)
    return render(request, 'users/customer_list.html', {'customers': customers})



@login_required
def profile(request):
    user = request.user
    customers = CustomerDetails.objects.filter(user=user)
    orders = Orders.objects.filter(user=user)

    # Add parsed item list to each order
    for order in orders:
        try:
            raw_items = json.loads(order.items_json)
            order.items_list = [
                {
                    'code': key,
                    'quantity': val[0],
                    'name': val[1],
                    'price': val[2]
                } for key, val in raw_items.items()
            ]
        except Exception:
            order.items_list = []

    context = {
        'customers': customers,
        'orders': orders
    }

    return render(request, 'users/profile.html', context)
