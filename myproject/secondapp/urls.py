from modelapp import views
from django.urls import path,include
from secondapp import views



urlpatterns = [

  path('ipltable/',views.ipltable),
  path('getprice/',views.getprice),
  path('total/',views.totalprice),

]
