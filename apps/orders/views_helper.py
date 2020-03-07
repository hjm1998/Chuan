from orders.models import Cart


def get_total_price_ordering(user_id, project_id):
    carts = Cart.objects.filter(c_user_id=user_id).filter(c_is_select=True).filter(c_goods__g_project_id=project_id)
    total = 0
    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.g_price
    return total


def get_total_price(user_id):
    carts = Cart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total = 0
    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.g_price
    return total


def get_cart_num(user_id):
    carts = Cart.objects.filter(c_user_id=user_id)
    num = 0
    for cart in carts:
        num += cart.c_goods_num
    return num
