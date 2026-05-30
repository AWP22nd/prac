import mysql.connector

# Connect to MySQL server (adjust host, user, password as needed)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
cursor = conn.cursor()

# Execute SQL statements
sql = """
-- Buat database
CREATE DATABASE IF NOT EXISTS db_siswa;
USE db_siswa;

-- Buat tabel siswa
CREATE TABLE siswa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nomor_induk VARCHAR(10) UNIQUE NOT NULL,
    nama VARCHAR(100) NOT NULL,
    jurusan VARCHAR(50) NOT NULL,
    tanggal_lahir DATE NOT NULL,
    alamat TEXT NOT NULL
);

-- Insert data contoh (opsional)
INSERT INTO siswa (nomor_induk, nama, jurusan, tanggal_lahir, alamat) VALUES
('12345678', 'Aditya Wahyu Permana', 'PPLG', '2010-06-22', 'Desa Brobot, Purbalingga');
"""

# Execute the SQL
for statement in sql.split(';'):
    if statement.strip():
        cursor.execute(statement)

# Commit and close
conn.commit()
cursor.close()
conn.close()