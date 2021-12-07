# EthereumDumpBalanceScript
A python script that transfers all ether to another wallet whenever a transaction is possible.  

Setup:
- Create an account on Infura and create a new Infura project. Go to project settings to see your project id. 
- Fill the variables in the .env file
  * WALLET_1_ADDRESS is the wallet whose balance you want to send to another wallet
  * WALLET_2_ADDRESS is the wallet you want receiving the ether
  * PRIVATE_KEY is wallet 1's private key
  * INFURA_API_KEY_MAIN is your Infura project's project id
- Run __init__.py

Requirements:
- Python
- Web3
- python-dotenv
