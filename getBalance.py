from SetupWeb3 import w3
from web3 import Web3
import Config

# Get variables
wallet1Address = Config.WALLET_1_ADDRESS
wallet2Address = Config.WALLET_2_ADDRESS
privateKey = Config.PRIVATE_KEY

# If balance changes, transfer it to new wallet
def transferEther():
	# Get web3 wallet addresses
	address1 = Web3.toChecksumAddress(wallet1Address)
	address2 = Web3.toChecksumAddress(wallet2Address)

	# Set amount to send and gas fees
	amount = w3.eth.getBalance(address1) - (21000 * (w3.toWei(1, "gwei")))
	nonce = w3.eth.getTransactionCount(address1, 'pending')
	gasFees = 21000 * (w3.toWei(1, "gwei"))

	# If balance changes, transfer it to new wallet
	if amount > gasFees:
		try:
			tx = {
				'nonce': nonce,
				'to': address2,
				'value': amount,
				'gas': 21000,
				'gasPrice': w3.toWei(1, "gwei")
			}

			# Sign and send the transaction
			signed_tx = w3.eth.account.signTransaction(tx, privateKey)
			tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
		
			print('Balance sent to wallet 2')
		except:
			print('Nothing sent')
	else:
		print('Nothing sent')