from modelapp import views
from django.urls import path,include




urlpatterns = [

  path('get/',views.getstudent),
  path('register/',views.register),
  path('simple/',views.simple),
  path('createuser/',views.submitform),




]
