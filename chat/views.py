from datetime import datetime
from typing import AsyncGenerator
from django.shortcuts import render, redirect
from django.http import HttpRequest, StreamingHttpResponse, HttpResponse, JsonResponse
from django.urls import reverse
from django.conf import settings
from twilio.rest import Client
from . import models

import json, random, asyncio, random, string

# Create your views here.
def broadcast_sms(request):
    message_to_broadcast = "Your verification number is " + compose_sms(6)
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        print(recipient)
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=(message_to_broadcast))
    return HttpResponse("Messages sent: " + message_to_broadcast, 200)

def compose_sms(size):
    random_chars = ''.join([random.choice(string.ascii_uppercase + 
                                          string.ascii_lowercase + 
                                          string.digits) 
                                          for n in range(size)])
    
    return random_chars