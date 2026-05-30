import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sekolah"
)


cursor = db.cursor()
"INSERT INTO siswa1 (id_siswa, nama, kelas, umur) VALUES ( 1 , 'Andi', '10A', 16)"

cursor.execute()

db.commit()
print("Data berhasil ditambahkan!")