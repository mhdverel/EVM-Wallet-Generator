print(r"""
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

            github.com/yourgithub
""")

from web3 import Web3
import os

# File untuk menyimpan wallet yang telah dibuat
wallets_file = "wallets_generated.txt"
generated_wallets = set()

# 🔍 Load existing wallets untuk menghindari duplikasi
if os.path.exists(wallets_file):
    with open(wallets_file, "r") as f:
        for line in f:
            generated_wallets.add(line.strip())

# 🎲 Fungsi untuk membuat wallet unik
def generate_wallet():
    while True:
        acct = Web3().eth.account.create()
        private_key = acct.key.hex()
        public_address = acct.address

        if public_address not in generated_wallets:
            generated_wallets.add(public_address)
            with open(wallets_file, "a") as f:
                f.write(public_address + "\n")
            return private_key, public_address

# 💾 Fungsi untuk menyimpan data ke file
def save_to_file(filename, data, description):
    with open(filename, "a") as f:
        f.write(data + "\n")
    os.chmod(filename, 0o600)  # 🔒 Proteksi file agar tidak mudah diakses

# 🚀 Main Process
def main():
    print("\n🎉 Let's generate some wallets! 🎉")
    try:
        num_wallets = int(input("🔢 Enter the number of wallets to generate: "))
        if num_wallets <= 0:
            print("⚠️ Please enter a valid positive number!")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    for i in range(1, num_wallets + 1):
        print(f"\n✨ Generating Wallet {i}/{num_wallets}... 🪄")
        private_key, public_address = generate_wallet()
        
        print(f"📌 Address: {public_address} ✅")
        
        save_to_file("public_address.txt", public_address, "Public Address")
        save_to_file("private_key.txt", private_key, "Private Key")
    
    print("\n🎉 All wallets generated successfully! 🎉")
    print("📂 Check 'public_address.txt' & 'private_key.txt' for details.")

if __name__ == "__main__":
    main()
