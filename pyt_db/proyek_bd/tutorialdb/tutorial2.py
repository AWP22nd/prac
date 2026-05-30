import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sekolah"
)

# if db.is_connected():
#     print("Koneksi berhasil!")

cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE siswa1(
        id_siswa INT PRIMARY KEY,
        nama VARCHAR(100),
        kelas VARCHAR(10),
        umur INT
    )
    """
)

print("Tabel berhasil dibuat!")