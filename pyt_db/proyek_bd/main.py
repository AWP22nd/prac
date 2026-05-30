import mysql.connector
from tabulate import tabulate # Opsional: supaya tabel di terminal rapi

# 1. Koneksi ke Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sekolah_db"
)

cursor = db.cursor()

def tambah_siswa():
    print("\n--- Input Data Siswa ---")
    nis = input("NIS: ")
    nama = input("Nama: ")
    tgl_lahir = input("Tanggal Lahir (YYYY-MM-DD): ")
    kelas = input("Kelas: ")
    alamat = input("Alamat: ")
    
    sql = "INSERT INTO siswa (nis, nama, tgl_lahir, kelas, alamat) VALUES (%s, %s, %s, %s, %s)"
    val = (nis, nama, tgl_lahir, kelas, alamat)
    
    cursor.execute(sql, val)
    db.commit()
    print(f"Berhasil menambahkan {nama}!")

def tampilkan_siswa():
    print("\n--- Data Siswa di Database ---")
    cursor.execute("SELECT * FROM siswa")
    results = cursor.fetchall()
    
    # Header Tabel
    headers = ["NIS", "Nama", "Tgl Lahir", "Kelas", "Alamat"]
    
    # Menampilkan menggunakan tabulate agar rapi
    print(tabulate(results, headers=headers, tablefmt="grid"))

# Menu Utama
while True:
    print("\n[1] Tambah Data")
    print("[2] Tampilkan Data")
    print("[0] Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_siswa()
    elif pilih == "2":
        tampilkan_siswa()
    elif pilih == "0":
        break
    else:
        print("Pilihan tidak tersedia.")


# Tutup koneksi database saat selesai
cursor.close()
db.close()