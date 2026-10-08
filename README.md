# Study_Kasus_6_Nila-Amelia-Nabilla

Nama: Nila Amelia Nabilla

NIM: 102

Kelas: C

# PENJELASAN PROGRAM

Program ini yaitu, Sistem Manajemen Inventaris Barang dibuat untuk membantu toko kelontong dalam mengelola data barang. Program menggunakan file JSON sebagai tempat penyimpanan data. Pengguna dapat menampilkan data barang, menambahkan data barang baru, dan keluar dari program. Data yang ditambahkan akan disimpan ke file JSON sehingga tetap tersedia saat program dijalankan kembali.

# import json dan path
<img width="704" height="85" alt="image" src="https://github.com/user-attachments/assets/ab2933df-a4f2-42e5-9460-7308ce234305" />

import json digunakan untuk mengaktifkan fungsi pengolahan file JSON pada Python. Sedangkan path digunakan untuk menentukan lokasi file tokokelontong.json yang digunakan sebagai tempat penyimpanan data inventaris.

# membaca data json
<img width="494" height="63" alt="image" src="https://github.com/user-attachments/assets/2a68e730-a463-4390-94be-b02afc84ec2f" />

Bagian ini digunakan untuk membuka dan membaca data yang terdapat dalam file JSON. Data yang telah dibaca menggunakan json.load kemudian disimpan ke dalam variabel data agar dapat digunakan oleh program.

# Function tampilkan data
<img width="500" height="190" alt="image" src="https://github.com/user-attachments/assets/1b31b96b-8e93-4019-9848-7b0e584e0e2f" />

fungsi tampilkan data digunakan untuk menampilkan seluruh data inventaris yang tersimpan. Perulangan for digunakan untuk mengambil setiap data barang, kemudian menampilkan nama, stok, dan harga barang.

# Function tambah data
<img width="399" height="187" alt="image" src="https://github.com/user-attachments/assets/27403fca-c04b-4bd4-a100-6738ea9db80d" />

Fungsi tambah data digunakan untuk menambahkan barang baru ke dalam data inventaris. Data yang dimasukkan berupa nama barang, stok, dan harga. append digunakan untuk memasukkan data baru ke dalam data.

# Function simpan file
<img width="502" height="115" alt="image" src="https://github.com/user-attachments/assets/839a2eef-0fa4-497e-8bf8-888eedc6d618" />

fungsi simpan file ini digunakan untuk menyimpan data yang sudah ditambahkan ke dalam file tokokelontong.json. json.dump agar data yang ada di dalam data dapat ditulis kembali ke file JSON. Dengan begitu, data yang baru ditambahkan tidak hanya tersimpan selama program berjalan, tetapi juga tetap ada ketika program dijalankan kembali.

# Perulangan dan menu program
<img width="575" height="171" alt="image" src="https://github.com/user-attachments/assets/97f16527-b14b-4017-8700-e89454af18e6" />

while True digunakan agar program dapat terus berjalan dan pengguna dapat menggunakan menu berkali-kali. Program memiliki tiga pilihan, yaitu Menampilkan Data, Menambah Data, dan Keluar.

# READ
<img width="330" height="77" alt="image" src="https://github.com/user-attachments/assets/8c09bb67-f379-4cfc-883c-ff03de4c9d2a" />

Jika memilih menu 1, program akan menjalankan function tampilkan data untuk menampilkan seluruh data barang yang tersedia.

# CREATE
<img width="529" height="182" alt="image" src="https://github.com/user-attachments/assets/fbd85f77-b65b-4256-9801-11dff610d4ac" />

Jika memilih menu 2, program akan meminta memasukkan nama barang, stok, dan harga. Data tersebut kemudian diproses oleh function tambah data dan dilanjutkan dengan function simpan file agar data langsung tersimpan ke file JSON.

# KELUAR
<img width="380" height="117" alt="image" src="https://github.com/user-attachments/assets/0f03964a-e59f-45d3-850f-da341cf02428" />

Jika memilih menu 3, program menampilkan pesan bahwa program selesai. Perintah break digunakan untuk menghentikan perulangan sehingga program berhenti.

# Pilihan tidak tersedia
<img width="435" height="79" alt="image" src="https://github.com/user-attachments/assets/3c1debd5-b83f-4105-97b5-8e4b052f76f5" />

Bagian else digunakan ketika memasukkan pilihan selain 1, 2, atau 3. Program akan memberikan pesan bahwa pilihan tersebut tidak tersedia dan kembali menampilkan menu.

# OUTPUT PROGRAM

# Menu utama
<img width="430" height="125" alt="image" src="https://github.com/user-attachments/assets/3cc49470-8fa1-466e-b24a-86860986bb1b" />

Output tersebut merupakan menu utama program. dapat memilih fitur yang ingin digunakan.

# READ
<img width="434" height="413" alt="image" src="https://github.com/user-attachments/assets/88e532ea-e6f2-4e3b-a89d-0d57b53e28f3" />

ika memilih menu 1, program menampilkan seluruh barang yang sebelumnya sudah tersimpan di file JSON, seperti nama barang, jumlah stok, dan harga.

# CREATE
<img width="432" height="285" alt="image" src="https://github.com/user-attachments/assets/d3954c95-cd7e-41b1-9b81-9fde8ac2ce59" />

Jika memilih menu 2, program meminta memasukkan data barang baru.
Output tersebut menunjukkan bahwa data barang berhasil ditambahkan dan kemudian disimpan ke dalam file JSON.

# ini output yang menunjukkan data berhasil ditambahkan.
<img width="432" height="513" alt="image" src="https://github.com/user-attachments/assets/e60afb1d-cc7b-4ba1-be88-4e7ccc61bb79" />

# Tampilan json sebelum data di tambah
<img width="235" height="216" alt="new6" src="https://github.com/user-attachments/assets/d881ddf7-9a71-4901-8edf-6aa6ec6883d3" />

# Tampilan json setelah data di tambah
<img width="422" height="551" alt="image" src="https://github.com/user-attachments/assets/984a1ca1-2ac7-4139-9d57-083f415727e2" />

# output keluar program
<img width="427" height="136" alt="image" src="https://github.com/user-attachments/assets/12ff6dc6-3e36-41aa-8598-4021b5b78f6c" />

Pada bagian ini ketika memilih menu 3 untuk keluar dari program. Program menampilkan pesan “Program selesai.”, kemudian perulangan while dihentikan dengan break, sehingga program berakhir.

# output ketika program dijalankan kembali
<img width="439" height="559" alt="image" src="https://github.com/user-attachments/assets/c3dee202-24a7-43c5-b943-c7dc7bc22a08" />

Setelah program dijalankan kembali, data indomie cabe ijo masih terdapat di dalam daftar inventaris. Ini menunjukkan bahwa data yang ditambahkan sebelumnya sudah tersimpan secara permanen di file JSON dan dapat dibaca kembali ketika program dijalankan.
