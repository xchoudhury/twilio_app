from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from twilio_app.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

@api_view(['GET'])
def send_sms(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.api.account.messages.create(
        to="+1111111111",
        from_=TWILIO_PHONE_NUMBER,
        body="Hello Person!"
    )
    data = {'status':'OK'}
    return Response(data)

@api_view(['GET', 'POST'])
def receive_sms(request):
    resp = MessagingResponse().message("Hello there person!")
    return str(resp)
