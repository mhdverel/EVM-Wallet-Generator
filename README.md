# 🚀 EVM Wallet Generator

## 📜 Deskripsi
**EVM Wallet Generator** adalah script Python untuk membuat dompet Ethereum Virtual Machine (EVM) secara otomatis. Script ini memiliki dua metode pembuatan wallet:
1. **`main.py`** → Menggunakan library `eth_account` dan `mnemonic`.
2. **`run.py`** → Menggunakan library `web3`.

Setiap metode menghasilkan **Public Address**, **Private Key**, dan **Seed Phrase**, serta menyimpannya dalam file terpisah untuk keamanan.

---

## 🎯 Fitur
✅ **Dua Metode Pembuatan Wallet** (`eth_account` & `web3`) 🔄  
✅ **Menghindari Duplikasi Wallet** 🛑  
✅ **Menyimpan Data ke File Terpisah** 🗂️  
✅ **Proteksi File Private Key & Seed Phrase** 🔒  
✅ **Mendukung Pembuatan Banyak Wallet Sekaligus** 🔢  

---

## 🛠️ Instalasi & Penggunaan

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/mhdverel/EVM-Wallet-Generator.git
cd EVM-Wallet-Generator
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Jalankan Script**

📌 **Menggunakan `eth_account` & `mnemonic` (main.py):**
```bash
python3 main.py
```

📌 **Menggunakan `web3` (run.py):**
```bash
python3 run.py
```

💡 **Ikuti instruksi di terminal untuk menentukan jumlah wallet yang ingin dibuat!**

---

## 📂 Output
Setiap wallet yang dibuat akan disimpan dalam file berikut:
- 📜 **public_address.txt** → Menyimpan alamat dompet publik.
- 🔑 **private_key.txt** → Menyimpan private key (jangan dibagikan!).
- 🔐 **seed_phrase.txt** → Menyimpan seed phrase untuk pemulihan dompet.

**Pastikan Anda menyimpan file-file ini dengan aman!** 🚨

---

## 🔥 Contoh Hasil Wallet
```
Public Address: 0x1234...abcd
Private Key: 0x5678...efgh
Seed Phrase: word1 word2 word3 ... word12
```

---

## ⚠️ Disclaimer
Script ini dibuat untuk **tujuan edukasi**. Penggunaan script ini sepenuhnya tanggung jawab pengguna. **Jangan gunakan untuk aktivitas ilegal!** 🚨

---

## 👨‍💻 Author
👤 **PEY**  
🔗 [GitHub](https://github.com/mhdverel)  
📩 **mhdverel@gmail.com**  

🚀 **Happy Coding!** 🎉

