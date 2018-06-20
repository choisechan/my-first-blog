#contract transaction code
import time
from web3 import Web3, IPCProvider, HTTPProvider
from web3.contract import ConciseContract

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

contract(account,customer,private_key)




