# EthereumDumpBalanceScript
- Script checks if the balance of an Ethereum Wallet can be sent to another address
- If the wallet has enough Ether for gas fees, it will send all of the Ether in the wallet to the second wallet

## Requirements:
- Python
- Web3
- python-dotenv

## Installing Python and Libraries
1. Download and install Python from [here](https://www.python.org/downloads/)
2. Download the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) file
3. Open a terminal/command prompt, cd to the folder containing the get-pip.py file and run:
 - Linux/MacOS: `python get-pip.py`
 - Windows: `py get-pip.py`
4. In your terminal/command prompt, cd to the folder you want to store the script in and run:
 - `git clone https://github.com/brianalbert7/EthereumDumpBalanceScript.git`
5. In your terminal/command prompt, cd to EthereumDumpBalanceScript and run:
 - `pip install web3` and `pip install python-dotenv`
 
## Setup:
- Create an account on Infura and a new Infura project. Go to project settings to see your project id. 
- Fill the variables in the .env file
  * WALLET_1_ADDRESS is the wallet whose balance you want to send to another wallet
  * WALLET_2_ADDRESS is the wallet you want receiving the ether
  * PRIVATE_KEY is wallet 1's private key
  * INFURA_API_KEY_MAIN is your Infura project's project id
- Run __init__.py

## Sources:
 - https://www.geeksforgeeks.org/how-to-install-pip-on-windows/?ref=lbp
 - https://www.youtube.com/watch?v=0rzDcair9rg
 - https://medium.com/coinmonks/how-to-build-a-python-app-that-texts-you-when-your-eth-balance-changes-a78baa4222e0
