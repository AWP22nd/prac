import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

# cara membuat database
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_sekolah")

print("Database berhasil dibuat!")

if db.is_connected():
    print("Koneksi berhasil!")
