from django.urls import path

from . import views

app_name="myitems"

urlpatterns = [
    path('',views.index,name="index")
]
