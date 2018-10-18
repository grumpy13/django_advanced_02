from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def create_view(request):
    form = StoreModelForm()
    if request.method == "POST":
        form = StoreModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


def store_detail(request, slug):
    context = {
        "store": Store.objects.get(slug=slug)
    }
    return render(request, 'store_detail.html', context)


