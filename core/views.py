from django.shortcuts import render

from item.models import Category,Item,PriorityTag

# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')

def item_search(request):
    query=request.GET.get('q')
    items=Item.objects.filter(name__icontains=query)
    context={'items':items,'query':query}
    return render(request,'core/search_result.html',context)