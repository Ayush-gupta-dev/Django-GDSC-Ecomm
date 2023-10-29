from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name="contact"),
    path('search/',views.item_search, name='item_search'),
    path('signup/',views.Signup,name="signup")
 
]
