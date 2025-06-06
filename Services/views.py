from django.http.response import HttpResponse , JsonResponse
from django.shortcuts import render
from django.db import transaction
from Services.models import Origincard , Moneytransfer
import os , json

def Fund_transfer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        card_from = data.get("card_from")
        card_to = data.get("card_to")
        amount = data.get("how much you want to transfer?")
        if len (card_from) != 16 or len(card_to) != 16 :
            return JsonResponse({"error = The card number must be 16 digits."} , status = 400)
        
        try: 
            amount = int(amount)  
        except ValueError:
            return JsonResponse({"error": "The transfer value must be a number."}, status=400)
        
        if amount <= 0 :
            return JsonResponse({"error = The amount must be greater than zero!"} , status = 400 )

        
        with transaction.atomic():

            if Origincard.inventory < amount :
                return JsonResponse({"error": "The origin card inventory is not sufficient."})
            
            Origincard.inventory -= amount
            Origincard.save()
            
    return JsonResponse({"message": "The transfer was successful."}, status=200)


            























def Financial_management(request):
    pass

def Paying_bills(request):
    pass
def Account_recharge(request):
    pass

def Box(request):
    pass

def big_box(request):
    pass

def SIMcard_charging(request):
    pass

def Invite_friends(request):
    pass

def Lawyers_Box(request):
    pass