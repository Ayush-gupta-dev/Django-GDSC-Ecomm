from django.shortcuts import render, redirect

from item.models import Category,Item

from .forms import SignupForm

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

def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()
    return render(request, 'core/signup.html',{
        'form':form
    })