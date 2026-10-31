import hashlib

# Password disimpan dalam bentuk hash, bukan teks asli
def buat_hash(teks):
    return hashlib.sha256(teks.encode()).hexdigest()

# "Database" sederhana: username -> hash password
users = {}

def daftar():
    username = input("Buat username: ")
    if username in users:
        print("Username sudah dipakai.")
        return
    password = input("Buat password: ")
    users[username] = buat_hash(password)
    print("Pendaftaran berhasil!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == buat_hash(password):
        print("Login berhasil! Selamat datang,", username)
    else:
        print("Username atau password salah.")

while True:
    print("\n1. Daftar\n2. Login\n3. Keluar")
    pilihan = input("Pilih: ")
    if pilihan == "1":
        daftar()
    elif pilihan == "2":
        login()
    elif pilihan == "3":
        break