from django.urls import path
from django.contrib.auth import views as authViews
from . import views
from .forms import LoginForm

app_name='core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name="contact"),
    path('search/',views.item_search, name='item_search'),
    path('signup/',views.Signup,name="signup"),
    path('logout/',views.logout, name='logout'),
    path('login/',authViews.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),name='login')
 
]
