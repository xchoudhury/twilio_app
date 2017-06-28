from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^sms/send/$',
        views.send_sms,
        name='send_sms'
    ),
    url(
        r'^sms/receive/$',
        views.receive_sms,
        name='receive_sms'
    ),
    
]
