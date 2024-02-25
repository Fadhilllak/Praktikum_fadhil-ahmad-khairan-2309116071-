import os
os.system('cls')

from prettytable import PrettyTable

class AlatSholat:
    no = 0

    def __init__(self, kode_barang, nama_barang, jenis, harga_jual):
        AlatSholat.no += 1
        self.no = f" ({AlatSholat.no:02d})"
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.jenis = jenis
        self.harga_jual = harga_jual

class PenjualanAlatSholat:
    def __init__(self):
        self.daftar_alat_sholat = []

    def tambah_alat_sholat(self, kode_barang, nama_barang, jenis, harga_jual):
        alat_sholat = AlatSholat(kode_barang, nama_barang, jenis, harga_jual)
        self.daftar_alat_sholat.append(alat_sholat)
        for i, alat_sholat in enumerate(self.daftar_alat_sholat, start=1):
            alat_sholat.no = f" ({i:02d})"

    def hapus_alat_sholat(self, kode_barang):
        for alat_sholat in self.daftar_alat_sholat:
            if alat_sholat.kode_barang == kode_barang:
                self.daftar_alat_sholat.remove(alat_sholat)
                break
        for i, alat_sholat in enumerate(self.daftar_alat_sholat, start=1):
            alat_sholat.no = f" ({i:02d})"

    def update_alat_sholat(self, kode_barang, **penjualan):
        for alat_sholat in self.daftar_alat_sholat:
            if alat_sholat.kode_barang == kode_barang:
                for key, value in penjualan.items():
                    if hasattr(alat_sholat, key):
                        setattr(alat_sholat, key, value)
                    else:
                        print(f"{key} tidak ditemukan pada alat sholat dengan kode {kode_barang}")
                break

    def tampilkan_data(self):
        table = PrettyTable()
        table.field_names = ["No", "Kode Barang", "Nama Barang", "Jenis", "Harga Jual"]
        for alat_sholat in self.daftar_alat_sholat:
            table.add_row([
                alat_sholat.no,
                alat_sholat.kode_barang,
                alat_sholat.nama_barang,
                alat_sholat.jenis,
                alat_sholat.harga_jual
            ])
        return table

    def generate_invoice(self):
        invoice_table = self.tampilkan_data()
        print("Invoice:")
        print(invoice_table)

    def tampilkan_menu(self):
        print("Menu:")
        print("1. Tambah Alat Sholat")
        print("2. Tampilkan Data Alat Sholat")
        print("3. Ubah Alat Sholat")
        print("4. Generate Invoice")
        print("5. Keluar")

# Buat instance PenjualanAlatSholat di sini
penjualan_alat_sholat = PenjualanAlatSholat()

def tambah_alat_sholat():
    kode_barang = input("Masukkan kode alat sholat: ")
    nama_barang = input("Masukkan nama alat sholat (sejadah, sarung, mukena, kopiah, tasbih): ")

    allowed_barang = ["sejadah", "sarung", "mukena", "kopiah", "tasbih"]
    while nama_barang.lower() not in allowed_barang:
        print("Nama barang tidak valid. Pilihan: sejadah, sarung, mukena, kopiah, tasbih")
        nama_barang = input("Masukkan nama alat sholat: ")

    jenis = input("Masukkan jenis alat sholat: ")
    
    while True:
        try:
            harga_jual = int(input("Masukkan harga jual alat sholat: "))
            break
        except ValueError:
            print("Harus Angka!")

    penjualan_alat_sholat.tambah_alat_sholat(kode_barang, nama_barang, jenis, harga_jual)

def ubah_alat_sholat():
    penjualan_alat_sholat.tampilkan_data()
    kode_barang = input("Masukkan kode alat sholat yang ingin diubah: ")
    field = input("Masukkan field yang ingin diubah (nama_barang, jenis, harga_jual): ")
    
    while True:
        try:
            new_value = int(input("Masukkan nilai baru: "))
            break
        except ValueError:
            print("Harus angka!")
    
    penjualan_alat_sholat.update_alat_sholat(kode_barang, **{field: new_value})

# Contoh penggunaan
while True:
    penjualan_alat_sholat.tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        tambah_alat_sholat()
    elif pilihan == '2':
        penjualan_alat_sholat.tampilkan_data()
    elif pilihan == '3':
        ubah_alat_sholat()
    elif pilihan == '4':
        penjualan_alat_sholat.generate_invoice()
    elif pilihan == '5':
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")
