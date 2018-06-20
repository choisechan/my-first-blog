from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from account.models import Account

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

class AccountLV(LoginRequiredMixin, ListView):
    template_name = 'account/account_list.html'
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

class AccountDV(DetailView):
   model = Account

def receit(request):
    return render(request, 'account/receit.html' , {})

def get_info(request):
    if request.method == "POST":
        form = gudok_ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
        return render(request, 'photo/gudok_add_success.html', {'form':form})
    else:
        account = Account.objects.get(owner=request.user)
        return render(request, 'account/account_list.html', {'account':account})
