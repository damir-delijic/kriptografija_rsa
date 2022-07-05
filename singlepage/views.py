from pydoc import plain
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from . import rsa
import json

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

rsa_system = -1

def generate_key(request, num):
    global rsa_system
    rsa_system = rsa.Rsa(num)
    
    response = json.dumps({
        'status': 'ok',
        'private_key': str(rsa_system.d),
        'public_key': str(rsa_system.e)
    })
    return HttpResponse(response)

@csrf_exempt
def encrypt(request):
    global rsa_system
    if rsa_system == -1:
        return HttpResponse(json.dumps({
        'status': 'ok',
        'result': 'Error, keys not generated.'
    }))
    plaintext = request.POST['text']
    cyphertext = rsa_system.ENCRYPT_MESSAFE(plaintext)
    response = json.dumps({
        'status': 'ok',
        'result': cyphertext
    })
    return HttpResponse(response)

@csrf_exempt
def decrypt(request):
    global rsa_system
    if rsa_system == -1:
        return HttpResponse(json.dumps({
        'status': 'ok',
        'result': 'Error, keys not generated.'
    }))
    cyphertext = request.POST['text']
    plaintext = rsa_system.DECRYPT_MESSAGE(cyphertext)
    response = json.dumps({
        'status': 'ok',
        'result': plaintext
    })
    return HttpResponse(response)
