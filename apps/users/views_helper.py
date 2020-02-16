import hashlib

from django.core.mail import send_mail
from django.template import loader

from Chuan.settings import EMAIL_HOST_USER, SERVER_HOST, SERVER_PORT, DEFAULT_FROM_EMAIL


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email_activate(username, receive, u_token):
    subject = '%s Chuan Activate' % username
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = [receive, ]
    data = {
        'username': username,
        'activate_url': 'http://{}:{}/users/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)
    }
    html_message = loader.get_template('user/activate.html').render(data)
    send_mail(subject=subject, message='', from_email=from_email,
              recipient_list=recipient_list, html_message=html_message,)
