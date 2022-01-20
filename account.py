from algosdk import mnemonic

class Account:
  def __init__(self,user_mnemonic:str) -> None:
    self.address = mnemonic.to_public_key(user_mnemonic)
    self.sk = mnemonic.to_private_key(user_mnemonic)

  def getPublicKey(self)->str:
    return self.address
  
  def getPrivateKey(self)->str:
    return self.sk
