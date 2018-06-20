from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from account.models import Account
#contract transaction code
import time
from web3 import Web3, IPCProvider, HTTPProvider
from web3.contract import ConciseContract
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.

class AlbumLV(ListView):
    model = Album
    def get_queryset(self):
        return Album.objects.filter(category=1)

class AlbumLV2(ListView):
    model = Album
    def get_queryset(self):
        return Album.objects.filter(category=2)

class AlbumLV3(ListView):
    model = Album
    def get_queryset(self):
        return Album.objects.filter(category=3)

class AlbumLV4(ListView):
    model = Album
    def get_queryset(self):
        return Album.objects.filter(category=4)

@csrf_exempt
@login_required
def buy(request):
    if request.method == "POST":
        account1 = Account.objects.get(owner=request.user)
        contract("0x47AEB7D85c1752ce6aaBDBd67A4E28334dDA8861", account1.account, account1.p_key)

        return render(request, 'photo/buy_ok.html', {'account1':account1} )
    else:
        return render(request, 'photo/buy_ok.html', {})



class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo




#--- Add/Change/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'origin', 'image', 'description','cnt','price','Subscription_ratings','purchase_after_sub']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = Photo
    fields = ['album', 'origin', 'image', 'description','cnt','price','Subscription_ratings','purchase_after_sub']
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = Photo
    success_url = reverse_lazy('photo:index')

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(LoginRequiredMixin, DeleteView) :
    model = Album
    success_url = reverse_lazy('photo:index')


#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from photo.forms import PhotoInlineFormSet

class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('photo:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))



def contract(account, customer, private_key):
   w3 = Web3(HTTPProvider("https://ropsten.infura.io/"))
   contract_address     = account
   wallet_private_key   =  private_key
   wallet_address       =  customer
   contract = w3.eth.contract(address = contract_address, abi='[ { "anonymous": false, "inputs": [ { "indexed": false, "name": "backer", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" }, { "indexed": false, "name": "isContribution", "type": "bool" } ], "name": "FundTransfer", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "to", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "EthTransfer", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "seller", "type": "address" }, { "indexed": false, "name": "item", "type": "string" } ], "name": "PurchaseItem", "type": "event" }, { "constant": false, "inputs": [ { "name": "seller", "type": "address" }, { "name": "item", "type": "string" } ], "name": "sendEthToSeller", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "tokenReturnEth", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function" }, { "inputs": [ { "name": "ifSuccessfulSendTo", "type": "address" }, { "name": "etherCostOfEachToken", "type": "uint256" }, { "name": "addressOfTokenUsedAsReward", "type": "address" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "beneficiary", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "price", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenReward", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
   nonce = w3.eth.getTransactionCount(wallet_address)
   private_key = Web3.toBytes(hexstr=wallet_private_key)
   w3.eth.enable_unaudited_features()
   gas_price = w3.toWei(21, 'gwei')

   contract_txn = contract.functions.sendEthToSeller(wallet_address, "je").buildTransaction({'gas' : 5000000, 'value' : 1000000000000000000, 'gasPrice': gas_price, 'nonce':nonce,})

   signed_txn = w3.eth.account.signTransaction(contract_txn, private_key)

   w3.eth.sendRawTransaction(signed_txn.rawTransaction)
   w3.toHex(w3.sha3(signed_txn.rawTransaction))
