import mysql.connector
import sys
from mysql.connector import Error
from datetime import datetime
import re

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''  # Sesuaikan dengan password MySQL Anda
        self.database = 'db_siswa'
        self.connection = None
    
    def connect(self):
        """Membuat koneksi ke database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Berhasil terhubung ke MySQL")
                return True
        except Error as e:
            print(f"Error koneksi: {e}")
            return False
    
    def disconnect(self):
        """Menutup koneksi database"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Koneksi ditutup")
    
    def get_all_siswa(self):
        """READ - Mengambil semua data siswa"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM siswa ORDER BY id DESC")
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error get_all_siswa: {e}")
            return []
    
    def check_unique_nomor_induk(self, nomor_induk):
        """Check if NIS is unique (available for new student)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM siswa WHERE nomor_induk = %s", (nomor_induk,))
            count = cursor.fetchone()[0]
            cursor.close()
            return count == 0
        except Error as e:
            print(f"Error check_unique_nomor_induk: {e}")
            return False
    
    def insert_siswa(self, nomor_induk, nama, jurusan, tanggal_lahir, alamat):
        """CREATE - Menambah data siswa baru"""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO siswa (nomor_induk, nama, jurusan, tanggal_lahir, alamat) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nomor_induk, nama, jurusan, tanggal_lahir, alamat))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error insert_siswa: {e}")
            return False
    
    def update_siswa(self, id, nomor_induk, nama, jurusan, tanggal_lahir, alamat):
        """UPDATE - Update data siswa"""
        try:
            cursor = self.connection.cursor()
            query = """
                UPDATE siswa 
                SET nomor_induk=%s, nama=%s, jurusan=%s, tanggal_lahir=%s, alamat=%s 
                WHERE id=%s
            """
            cursor.execute(query, (nomor_induk, nama, jurusan, tanggal_lahir, alamat, id))
            self.connection.commit()
            rowcount = cursor.rowcount
            cursor.close()
            return rowcount > 0
        except Error as e:
            print(f"Error update_siswa: {e}")
            return False
    
    def delete_siswa(self, id):
        """DELETE - Hapus data siswa"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM siswa WHERE id=%s"
            cursor.execute(query, (id,))
            self.connection.commit()
            rowcount = cursor.rowcount
            cursor.close()
            return rowcount > 0
        except Error as e:
            print(f"Error delete_siswa: {e}")
            return False