from merchant.models import Merchant


def get_merchant_order_status(status):
    if status == 1:
        return None
    elif status == 2:
        return ['待发货', '立即发货']
    elif status == 3:
        return ['待收货', '等待收货']
    elif status == 4:
        return ['已完成', '订单已完成']
    elif status == 5:
        return ['已评价', '评价']


def get_merchant_login_status(m_id, data):
    merchant = Merchant.objects.get(pk=m_id)
    data['merchant_name'] = merchant.m_merchantName
    data['is_login'] = True
