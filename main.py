print("""
🚀 Welcome to EVM Wallet Generator! 🚀

 ██▓███  ▓█████▓██   ██▓▓█████  ███▄    █   ▄████ 
▓██░  ██▒▓█   ▀ ▒██  ██▒▓█   ▀  ██ ▀█   █  ██▒ ▀█▒
▓██░ ██▓▒▒███    ▒██ ██░▒███   ▓██  ▀█ ██▒▒██░▄▄▄░
▒██▄█▓▒ ▒▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ ▓██▒  ▐▌██▒░▓█  ██▓
▒██▒ ░  ░░▒████▒ ░ ██▒▓░░▒████▒▒██░   ▓██░░▒▓███▀▒
▒▓▒░ ░  ░░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░░ ▒░   ▒ ▒  ░▒   ▒ 
░▒ ░      ░ ░  ░▓██ ░▒░  ░ ░  ░░ ░░   ░ ▒░  ░   ░ 
░░          ░   ▒ ▒ ░░     ░      ░   ░ ░ ░ ░   ░ 
            ░  ░░ ░        ░  ░         ░       ░ 
                ░ ░                                

        github.com/mhdverel
""")

from eth_account import Account
from mnemonic import Mnemonic
import os

# Enable HD Wallet features
Account.enable_unaudited_hdwallet_features()

def generate_wallet():
    # Generate Mnemonic Phrase
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=256)
    
    # Generate Account from Mnemonic
    acct = Account.from_mnemonic(seed_phrase)
    private_key = acct.key.hex()
    public_address = acct.address
    
    return seed_phrase, private_key, public_address

def save_to_file(filename, data):
    with open(filename, "a") as f:  # Append mode to keep all wallets in one file
        f.write(data + "\n")
    os.chmod(filename, 0o600)  # Set file permissions to read/write owner only

def main():
    print("\n🚀 Welcome to EVM Wallet Generator! 🚀")
    try:
        num_wallets = int(input("🔢 Enter the number of wallets to generate: "))
        if num_wallets <= 0:
            print("⚠️ Please enter a valid positive number!")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    for i in range(1, num_wallets + 1):
        print(f"\n✨ Generating Wallet {i}/{num_wallets}...")
        seed_phrase, private_key, public_address = generate_wallet()
        
        print(f"📌 Wallet Address: {public_address}")
        print("✅ Public address, private key, and seed phrase are saved in separate files.")
        
        # Save to respective files
        save_to_file("address_wallet.txt", public_address)
        save_to_file("private_key.txt", private_key)
        save_to_file("seed_phrase.txt", seed_phrase)
    
    print("\n🎉 Wallet generation completed! 🎉")

if __name__ == "__main__":
    main()
