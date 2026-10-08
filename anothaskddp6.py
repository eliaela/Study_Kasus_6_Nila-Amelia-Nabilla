import json

path = r"C:\Users\ASUS\.vscode\tokokelontong.py\tokokelontong.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)


def tampilkan_data():
    print("\n--- Data Inventaris Barang ---")
    for barang in data:
        print("Nama :", barang["nama"])
        print("Stok :", barang["stok"])
        print("Harga:", barang["harga"])
        print()


def tambah_data(nama, stok, harga):
    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga
    })
    return "Data barang ditambah!"


def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Tersimpan ke tokokelontong.json!"


while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
    print("1. Menampilkan Data")
    print("2. Menambah Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        stok = int(input("Masukkan stok barang: "))
        harga = int(input("Masukkan harga barang: "))

        print("\n", tambah_data(nama, stok, harga))
        print("\n", simpan_file())

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")