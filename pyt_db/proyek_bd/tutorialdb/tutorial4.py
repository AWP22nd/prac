import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tutorial3"
)

cursor = db.cursor()
show_data = "SELECT * FROM perpus3"
cursor.execute(show_data)

# menampilkan isi dari db dgn method fetchall
# results = cursor.fetchall()
# for i in results:
#     print(i)

# # dgn method fetchone
results = cursor.fetchone()
print(results)

# # semua
print("===============================")
print("======Data ditampilkan!========")
print("===============================")

while results is not None:
    print(results)  
    results = cursor.fetchone()

# # delete data
# cursor = db.cursor()
# delete = "DELETE FROM perpus3 WHERE id = %s"
# val = (2, )
# cursor.execute(delete, val)

# db.commit()
# print("Data berhasil dihapus!")