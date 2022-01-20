from algo_client import getAlgodClient, AlgodClient
from algosdk.future import transaction
from account import Account
from dextoolsmain_data import data

global SENDER_MN 
global SENDER_AC 

# Input your mnemonic
SENDER_MN = ""
SENDER_AC = Account(SENDER_MN)


def fundXET(client:AlgodClient,receiver):
  '''
  Functionality to fund account with 1000 dummy XETs

  '''
  xet_id = 283820866
  raw_txns = []

  for i in range(0,len(receiver)):
      receiver_address = receiver[i]["address"]
      amount = receiver[i]["amt"]*1000000000
      fund_xet_txn = transaction.AssetTransferTxn(sender=SENDER_AC.getPublicKey(),sp=client.suggested_params(),receiver=receiver_address,index=xet_id,amt=amount)
      raw_txns.append(fund_xet_txn)
 
  transaction.assign_group_id(raw_txns)
  signed_txn = []
  for i in range(0,len(raw_txns)):
    signed_fundXET_txn = raw_txns[i].sign(SENDER_AC.getPrivateKey())
    signed_txn.append(signed_fundXET_txn)
  client.send_transactions(signed_txn)

if __name__ == "__main__":
  client = getAlgodClient()
  receiver_ac = data
  fundtxinfo = fundXET(client,receiver_ac)
  print(fundtxinfo)
  
