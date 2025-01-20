import random
import string
from mnemonic import Mnemonic
from eth_account import Account
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic as BTCMnemonic

# Enable unaudited HD wallet features for eth_account
Account.enable_unaudited_hdwallet_features()

# Generate EVM-Compatible Wallet
def generate_evm_wallet():
    # Generate a mnemonic
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # 12-word seed phrase

    # Generate wallet from seed
    acct = Account.from_mnemonic(seed_phrase)
    private_key = acct.key.hex()
    address = acct.address

    return seed_phrase, private_key, address

# Generate Bitcoin Wallet
def generate_bitcoin_wallet():
    wallet_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    mnemonic = BTCMnemonic().generate()
    wallet = Wallet.create(wallet_name, keys=mnemonic, witness_type='segwit', network='bitcoin')
    private_key = wallet.get_key().wif
    address = wallet.get_key().address
    return mnemonic, private_key, address

# Main generator function
def generate_wallets(chains):
    wallets = []
    for chain in chains:
        if chain.lower() == "evm":
            seed, private_key, address = generate_evm_wallet()
            wallets.append({"chain": "EVM-Compatible", "mnemonic": seed, "private_key": private_key, "address": address})
        elif chain.lower() == "bitcoin":
            mnemonic, private_key, address = generate_bitcoin_wallet()
            wallets.append({"chain": "Bitcoin", "mnemonic": mnemonic, "private_key": private_key, "address": address})
        else:
            print(f"Chain '{chain}' is not supported.")
    return wallets

def main():
    # Specify the blockchains for which you want to generate wallets
    supported_chains = ["EVM", "Bitcoin"]  # Add or remove as needed

    print("Generating wallets...\n")
    wallets = generate_wallets(supported_chains)

    # Display the generated wallets
    for wallet in wallets:
        print(f"Chain: {wallet['chain']}")
        if "mnemonic" in wallet:
            print(f"Seed Phrase: {wallet['mnemonic']}")
        print(f"Private Key: {wallet['private_key']}")
        print(f"Address: {wallet['address']}\n")

if __name__ == "__main__":
    main()
