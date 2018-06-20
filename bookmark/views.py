from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin
from account.models import Account
from bookmark.models import Bookmark
from photo.models import Photo
#contract transaction code
import time
from web3 import Web3, IPCProvider, HTTPProvider
from web3.contract import ConciseContract
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

class BookmarkLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_list.html'
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkDV(DetailView):
   model = Bookmark

class SubGroupLV(ListView):
    model = SubGroup

class SubGroupDV(DetailView):
    model = SubGroup

class SubListLV(ListView):
    model = SubList

class SubListDV(DetailView):
    model = SubGroup

@login_required
@csrf_exempt
def add(request):
    account1 = Account.objects.get(owner=request.user)
    contract("0x47AEB7D85c1752ce6aaBDBd67A4E28334dDA8861", account1.account, account1.p_key)
    bookmark = Bookmark.objects.filter(owner=request.user)
    for item in bookmark:
        item.state="결재"
        item.save()
    bookmark = Bookmark.objects.filter(owner=request.user, state="결재")
    for item in bookmark:
        item.maker = Photo.objects.filter(album=item.title)[1].origin
        item.save()
    return render(request, 'bookmark/bookmark_change_list.html', {'bookmark':bookmark} )
    #렌더링은 평가창으로

#def rate(request):
#    return render(request, 'bookmark/bookmark_subScribeList.html', {} )

def buy_subscribe(request): #구매화면 띄우기
    bookmark = Bookmark.objects.filter(owner=request.user)
    return render(request, 'bookmark/bookmark_list.html', {'bookmark': bookmark})

def subscribing_list(request): # 평가창 띄우기
    bookmark = Bookmark.objects.filter(owner=request.user, state="결재")
    return render(request, 'bookmark/bookmark_change_list.html', {'bookmark' : bookmark})



class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title','price' ,'amount']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView) :
    model = Bookmark
    fields = ['title','amount' ,'star']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

def buy_subscribe(request):
    bookmark = Bookmark.objects.filter(owner=request.user)

    return render(request, 'bookmark/bookmark_list.html', {'bookmark': bookmark})


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
