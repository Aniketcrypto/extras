import secrets
import mnemonic

def generate_seed_phrase():
    mnemo = mnemonic.Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # Generates a 12-word seed phrase
    return seed_phrase

def main():
    print("Generating Wallet...\n")
    seed_phrase = generate_seed_phrase()
    print(f"Seed Phrase: {seed_phrase}")

if __name__ == "__main__":
    main()
