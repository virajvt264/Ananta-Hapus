from django.shortcuts import render
from oauthlib.uri_validate import query

from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomerDetails



def home(request):
    allProds=[]
    catprods = Product.objects.values('category', 'id')
    cats = {items['category'] for items in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    context={'allProds':allProds}
    return  render(request, 'mango_shop/index.html',context)


def about(request):
    return  render(request, 'mango_shop/about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name =  request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc =  request.POST.get('desc', '')
        contact= Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return  render(request, 'mango_shop/contact.html', {'thank':thank})


def tracking(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no items"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'mango_shop/tracking.html')


def product(request, myid):
    products=Product.objects.filter(id=myid)
    return  render(request, 'mango_shop/product.html', {'products':products[0]})


def gallary(request):
    return render(request, 'mango_shop/gallary.html')

def searchmatch(query, item):
    '''return true only if query matches in item'''
    if query in item.description.lower() or query in item.category.lower() or query in item.product_name.lower():
        return True
    else:
        return False

def products(request):
    allProds = []
    products = Product.objects.all()
    prod = {items for items in products}
    for product in prod:
        allProds.append(product)

    context = {'allProds': allProds}
    return render(request, 'mango_shop/products.html', context)

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {items['category'] for items in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchmatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    context = {'allProds': allProds}
    return render(request, 'mango_shop/index.html', context)

# @login_required
# def checkout(request):
#     if request.method == "POST":
#         print(request)
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amount', '')
#         email = request.POST.get('email', '')
#         address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone= request.POST.get('phone', '')
#         Order = Orders(items_json=items_json, name=name, email=email, address=address,
#                        city=city,state=state, zip_code=zip_code,  phone=phone, amount=amount)
#         Order.save()
#         update = OrderUpdate(order_id=Order.order_id, update_desc="The order has been placed")
#         update.save()
#         thank = True
#         id =Order.order_id
#         return  render(request, 'mango_shop/checkout.html', {'thank':thank, 'id':id})
#     return  render(request, 'mango_shop/checkout.html')





@login_required
def checkout(request):
    if request.method == "POST":
        print(request)
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        # Save main order
        order = Orders(
            user=request.user,
            items_json=items_json,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
            amount=amount
        )
        order.save()

        # Save order update log
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()

        thank = True
        id = order.order_id
        customers = CustomerDetails.objects.all()

        context = {
            'thank': thank,
            'id': id,
            'customers': customers
        }
        return render(request, 'mango_shop/checkout.html', context)

    # GET request
    user = request.user
    customers = CustomerDetails.objects.filter(user=user)
    return render(request, 'mango_shop/checkout.html', {'customers': customers})




from .models import Orders

@login_required
def profile(request):
    user = request.user
    customers = CustomerDetails.objects.filter(user=user)
    orders = Orders.objects.filter(user=user)
    return render(request, 'mango_shop/profile_user.html', {'customers': customers, 'orders': orders})


