import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sekolah"
)
# NO 1
# cursor = db.cursor()
# cursor.execute("SELECT * FROM siswa1")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 2
# cursor = db.cursor()
# cursor.execute("SELECT nama, kelas FROM siswa1 WHERE umur > 15")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 3
# cursor = db.cursor()
# cursor.execute("SELECT * FROM nilai WHERE mapel = 'Matematika'")
# results = cursor.fetchall()
# for row in results:
#     print(row)
# NO 4
# cursor = db.cursor()
# cursor.execute("SELECT siswa1.nama, nilai.mapel, nilai.nilai FROM siswa1 JOIN nilai ON siswa1.id_siswa = nilai.id_siswa")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 5
# cursor = db.cursor()
# cursor.execute("SELECT siswa1.nama, AVG(nilai.nilai) AS rata_rata FROM siswa1 JOIN nilai ON siswa1.id_siswa = nilai.id_siswa GROUP BY siswa1.nama")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 6
# cursor = db.cursor()
# cursor.execute("SELECT siswa1.nama, nilai.nilai FROM siswa1 JOIN nilai ON siswa1.id_siswa = nilai.id_siswa WHERE nilai.nilai > 85")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 7
# cursor = db.cursor()
# cursor.execute("SELECT siswa1.nama, nilai.nilai FROM siswa1 JOIN nilai ON siswa1.id_siswa = nilai.id_siswa WHERE nilai.nilai = (SELECT MAX(nilai) FROM nilai)")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 8
# cursor = db.cursor()
# cursor.execute("SELECT kelas, COUNT(*) AS jumlah_siswa FROM siswa1 GROUP BY kelas")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 9
# cursor = db.cursor()
# cursor.execute("SELECT siswa1.nama FROM siswa1 LEFT JOIN nilai ON siswa1.id_siswa = nilai.id_siswa WHERE nilai.nilai IS NULL")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# NO 10
# cursor = db.cursor()
# cursor.execute("INSERT INTO siswa1 (id_siswa, nama, kelas, umur) VALUES (5, 'Eda', '10B', 17)")
# db.commit()
# print("Data berhasil ditambahkan!")

# NO 11
# cursor = db.cursor()
# cursor.execute("UPDATE nilai SET nilai = 95 WHERE id_nilai = 1")
# db.commit()
# print("Data berhasil diperbarui!")

# NO 12
# cursor = db.cursor()
# cursor.execute("DELETE FROM siswa1 WHERE id_siswa = 5")
# db.commit()
# print("Data berhasil dihapus!")