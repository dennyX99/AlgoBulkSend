# AlgoBulkSend

### Install Python Algorand SDK
`pip install py-algorand-sdk`

### Steps to be followed for the transfer
1. Add your mnemonic in the `main.py`
2. Create a developer account in purestake and add the API token in `algo_client.py`
3. Should add all the address and token amounts in `dextoolsmain_data.py`
4. Maximum 16 transactions can be grouped togather.
5. `xet_optin_check.py` helps to check whether the listed addresses are opted in or not.
6. Verify all the token amounts
7. `python main.py` to transfer the tokens.
