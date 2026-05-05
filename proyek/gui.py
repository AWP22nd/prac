import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit,
                             QLabel, QDateEdit, QHeaderView, QMessageBox, QComboBox)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont
from database import Database

class siswaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.current_edit_id = None
        self.initUI()
        self.db.connect()
        self.load_data()
    
    def initUI(self):
        """Inisialisasi tampilan GUI"""
        self.setWindowTitle('Manajemen Data siswa')
        self.setGeometry(100, 100, 1000, 700)
        
        # Widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout utama
        main_layout = QVBoxLayout()
        
        # Form input
        form_layout = QHBoxLayout()
        
        # Nama
        self.lbl_nama = QLabel('Nama:')
        self.lbl_nama.setFont(QFont('Arial', 10, QFont.Bold))
        form_layout.addWidget(self.lbl_nama)
        self.txt_nama = QLineEdit()
        self.txt_nama.setPlaceholderText('Masukkan nama lengkap...')
        self.txt_nama.setMinimumWidth(150)
        form_layout.addWidget(self.txt_nama)
        
        # Jurusan
        self.lbl_jurusan = QLabel('Jurusan:')
        self.lbl_jurusan.setFont(QFont('Arial', 10, QFont.Bold))
        form_layout.addWidget(self.lbl_jurusan)
        self.combo_jurusan = QComboBox()
        self.combo_jurusan.addItems(['AP', 'APHP', 'AT', 
                                   'PPLG', 'TO'])
        form_layout.addWidget(self.combo_jurusan)
        
        # Tanggal Lahir
        self.lbl_tgl = QLabel('Tgl Lahir:')
        self.lbl_tgl.setFont(QFont('Arial', 10, QFont.Bold))
        form_layout.addWidget(self.lbl_tgl)
        self.date_tgl = QDateEdit()
        self.date_tgl.setDate(QDate.currentDate())
        self.date_tgl.setCalendarPopup(True)
        self.date_tgl.setMinimumDate(QDate(1900, 1, 1))
        self.date_tgl.setMaximumDate(QDate.currentDate())
        form_layout.addWidget(self.date_tgl)
        
        # Alamat
        self.lbl_alamat = QLabel('Alamat:')
        self.lbl_alamat.setFont(QFont('Arial', 10, QFont.Bold))
        form_layout.addWidget(self.lbl_alamat)
        self.txt_alamat = QLineEdit()
        self.txt_alamat.setPlaceholderText('Masukkan alamat lengkap...')
        self.txt_alamat.setMinimumWidth(200)
        form_layout.addWidget(self.txt_alamat)
        
        main_layout.addLayout(form_layout)
        
        # Tombol-tombol
        btn_layout = QHBoxLayout()
        self.btn_tambah = QPushButton('Tambah Data')
        self.btn_tambah.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.btn_tambah.clicked.connect(self.tambah_data)
        
        self.btn_edit = QPushButton('Edit Data')
        self.btn_edit.setStyleSheet("background-color: #2196F3; color: white; font-weight: bold;")
        self.btn_edit.clicked.connect(self.edit_data)
        self.btn_edit.setEnabled(False)
        
        self.btn_hapus = QPushButton('Hapus Data')
        self.btn_hapus.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;")
        self.btn_hapus.clicked.connect(self.hapus_data)
        self.btn_hapus.setEnabled(False)
        
        self.btn_refresh = QPushButton('Refresh')
        self.btn_refresh.setStyleSheet("background-color: #FF9800; color: white; font-weight: bold;")
        self.btn_refresh.clicked.connect(self.load_data)
        
        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_hapus)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_refresh)
        
        main_layout.addLayout(btn_layout)
        
        # Tabel data
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Nama', 'Jurusan', 'Tgl Lahir', 'Alamat'])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        
        self.table.itemSelectionChanged.connect(self.on_table_selection_changed)
        main_layout.addWidget(self.table)
        
        central_widget.setLayout(main_layout)
    
    def validate_input(self):
        """Validasi input form"""
        nama = self.txt_nama.text().strip()
        jurusan = self.combo_jurusan.currentText()
        tanggal = self.date_tgl.date().toString('yyyy-MM-dd')
        alamat = self.txt_alamat.text().strip()
        
        if not nama:
            QMessageBox.warning(self, 'Peringatan', 'Nama tidak boleh kosong!')
            self.txt_nama.setFocus()
            return False
        
        if not jurusan:
            QMessageBox.warning(self, 'Peringatan', 'Jurusan harus dipilih!')
            return False
        
        if not alamat:
            QMessageBox.warning(self, 'Peringatan', 'Alamat tidak boleh kosong!')
            self.txt_alamat.setFocus()
            return False
        
        return True
    
    def load_data(self):
        """Load data ke tabel"""
        data = self.db.get_all_siswa()
        self.table.setRowCount(len(data))
        
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                if col_idx == 0:  # ID column
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable) # pyright: ignore[reportUndefinedVariable]
                self.table.setItem(row_idx, col_idx, item)
        
        self.clear_form()
        self.btn_edit.setEnabled(False)
        self.btn_hapus.setEnabled(False)
    
    def tambah_data(self):
        """Tambah data siswa"""
        if not self.validate_input():
            return
        
        nama = self.txt_nama.text().strip()
        jurusan = self.combo_jurusan.currentText()
        tanggal = self.date_tgl.date().toString('yyyy-MM-dd')
        alamat = self.txt_alamat.text().strip()
        
        if self.db.insert_siswa(nama, jurusan, tanggal, alamat):
            QMessageBox.information(self, 'Sukses', 'Data siswa berhasil ditambahkan!')
            self.load_data()
        else:
            QMessageBox.critical(self, 'Error', 'Gagal menambahkan data!')
    
    def edit_data(self):
        """Edit data siswa"""
        if not self.validate_input() or not self.current_edit_id:
            return
        
        nama = self.txt_nama.text().strip()
        jurusan = self.combo_jurusan.currentText()
        tanggal = self.date_tgl.date().toString('yyyy-MM-dd')
        alamat = self.txt_alamat.text().strip()
        
        if self.db.update_siswa(self.current_edit_id, nama, jurusan, tanggal, alamat):
            QMessageBox.information(self, 'Sukses', 'Data siswa berhasil diupdate!')
            self.load_data()
        else:
            QMessageBox.critical(self, 'Error', 'Gagal mengupdate data!')
    
    def hapus_data(self):
        """Hapus data siswa"""
        reply = QMessageBox.question(self, 'Konfirmasi', 
                                   'Apakah Anda yakin ingin menghapus data ini?',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes and self.current_edit_id:
            if self.db.delete_siswa(self.current_edit_id):
                QMessageBox.information(self, 'Sukses', 'Data siswa berhasil dihapus!')
                self.load_data()
            else:
                QMessageBox.critical(self, 'Error', 'Gagal menghapus data!')
    
    def on_table_selection_changed(self):
        """Event saat row tabel dipilih"""
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            self.current_edit_id = int(self.table.item(row, 0).text())
            self.txt_nama.setText(self.table.item(row, 1).text())
            self.combo_jurusan.setCurrentText(self.table.item(row, 2).text())
            self.date_tgl.setDate(QDate.fromString(self.table.item(row, 3).text(), 'yyyy-MM-dd'))
            self.txt_alamat.setText(self.table.item(row, 4).text())
            self.btn_edit.setEnabled(True)
            self.btn_hapus.setEnabled(True)
    
    def clear_form(self):
        """Clear form input"""
        self.txt_nama.clear()
        self.combo_jurusan.setCurrentIndex(0)
        self.date_tgl.setDate(QDate.currentDate())
        self.txt_alamat.clear()
        self.current_edit_id = None
    
    def closeEvent(self, event):
        """Event saat aplikasi ditutup"""
        self.db.disconnect()
        event.accept()