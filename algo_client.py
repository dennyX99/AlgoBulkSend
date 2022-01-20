from algosdk.v2client.algod import AlgodClient

ALGOD_ADDRESS = "https://mainnet-algorand.api.purestake.io/ps2"
# Input Algod Token, created from purestake. https://developer.purestake.io/
ALGOD_TOKEN = ""
headers={
  "X-API-Key": ALGOD_TOKEN,
}

def getAlgodClient() -> AlgodClient:
  return AlgodClient(algod_token=ALGOD_TOKEN,algod_address=ALGOD_ADDRESS,headers=headers)
  