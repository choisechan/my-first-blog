from django.shortcuts import render
from gudok.models import gudok_Album, gudok_Item
from django.utils import timezone
from .models import gudok_Item, gudok_Album
from .forms import gudok_ItemForm
# Create your views here.


def gudok_add(request):
    if request.method == "POST":
        form = gudok_ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
        return render(request, 'photo/gudok_add_success.html', {'form':form})
    else:
        form = gudok_ItemForm()
        return render(request, 'photo/gudok_add.html', {'form':form})
