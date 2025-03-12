from django.views import path
from .views import Fund_transfer,Financial_management,Paying_bills,Account_recharge,Box,big_box,SIMcard_charging,Invite_friends,Lawyers_Box

Urlpatterns = [
  path('',Financial_management),
  path('', Paying_bills),
  path('transfer', Fund_transfer),
  path('', Account_recharge),
  path('', Box),
  path('', big_box),
  path('', SIMcard_charging),
  path('', Invite_friends),
  path('', Lawyers_Box),

 ]
