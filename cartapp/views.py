from django.shortcuts import render, redirect
from mainApp.utils import menu
from .models import CartItem
def get_items_cart(request):
    user_id = request.user.pk

    items = CartItem.objects.filter(user_id=user_id)
    all_price = sum(map(lambda x: x.product.price*x.quantity, items))
    context = {
        'menu': menu,
        'items': items,
        'all_price': all_price,
    }

    return render(request, 'cartapp/cart_page.html', context)


def update_cart(request):
    if request.method == 'POST':
        metod, product_id = request.POST['btn'].split('_')
        if metod == 'add':
            add_item_cart(request, product_id)
        elif metod == 'remove':
            remove_item_cart(request, product_id)
        else:
            pass
        return redirect(request.META['HTTP_REFERER'])


def add_item_cart(request, product_id):
    if request.method == 'POST':
        user_id = request.user.pk
        #product_id = request.POST['btn']
        for i, j in request.POST.items():
            print(f'{i} = {j}')
        try:
            item = CartItem.objects.get(user_id=user_id, product_id=product_id)
            item.quantity+= 1
        except:
            item = CartItem(user_id=user_id, product_id=product_id)
        item.save()
        #return redirect(request.META['HTTP_REFERER'])

def remove_item_cart(request, product_id):
    if request.method == 'POST':
        user_id = request.user.pk
        #product_id = request.POST['product_id']
        print(f'product_id = {product_id}')
        item = CartItem.objects.get(user_id=user_id, product_id=product_id)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        #return redirect(request.META['HTTP_REFERER'])
