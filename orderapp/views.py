from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from cartapp.models import CartItem
from .models import *

def add_order(request):
    """
        Функция добавления заказа в БД и удаление позиций из козины пользователя
    """
    # for i, j in dict(request.POST).items():
    #     print(f'{i} = {j}')
    # print(dict(request.POST)['product_id'])
    if request.method == 'POST':
        user = request.user
        data_post = dict(request.POST)
        for_order = data_post['for-order']
        print(for_order)
        products_id = map(int, data_post['product_id'])
        if any(map(lambda x: x=='on', for_order)):
            order = Order(user=user)
            order.save()
            for product_id, check in zip(products_id, for_order):
                if check == 'on':
                   print(1)
                   item_cart = CartItem.objects.get(user=user, product_id=product_id)
                   item_order = Item_Order(order=order, product_id=product_id, quantity=item_cart.quantity)
                   item_order.save()
                   item_cart.delete()
                else:
                    pass
    return redirect(request.META['HTTP_REFERER'])
