from getBalance import transferEther
from SetupWeb3 import w3
from web3 import Web3
import Config
import time

def loop_main(poll_interval):
    while True:
        transferEther()
        time.sleep(poll_interval)

def main():
    loop_main(2)

main()