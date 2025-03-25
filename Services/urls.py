from django.views import path
from .views import Fund_transfer,Financial_management,Paying_bills,Account_recharge,Box,big_box,SIMcard_charging,Invite_friends,Lawyers_Box

Urlpatterns = [
  path('transfer', Fund_transfer),
  path('Paying_bills', Paying_bills),
  path('Box', Box),
  path('Financial_management', Financial_management),
  path('Account_recharge', Account_recharge),
  path('big_box', big_box),
  path('SIMcard_charging', SIMcard_charging),
  path('Invite_friends', Invite_friends),
  path('Lawyers_Box', Lawyers_Box),
 ]
