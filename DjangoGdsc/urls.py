
from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.views import contact
from django.conf import settings
from django.conf.urls.static import static
from core.views import item_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/',include('item.urls')),
    path('',index,name='index'),
    path('contact/',contact,name="contact"),
    path('search/',item_search, name='item_search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
