# ===========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama   : Fahrizal Azis
# NIM    : J0403251151
# Kelas  : TPL A1
# ===========================================================

NAMA_FILE = "stok_barang.txt"

# -----------------------------
# Fungsi: Membaca data dari file
# -----------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output: Dictionary stok_dict
    """
    stok_dict = {}

    try:
        # TODO: Buka file dan baca seluruh baris
        with open(nama_file, "r", encoding="utf-8") as f:
            for line in f:
                # TODO: Untuk setiap baris: strip, split, simpan ke dictionary
                line = line.strip()
                if not line: continue  # Lewati baris kosong jika ada
                
                parts = line.split(",")
                if len(parts) == 3:
                    kode = parts[0]
                    nama = parts[1]
                    stok = int(parts[2])
                    
                    stok_dict[kode] = {"nama": nama, "stok": stok}
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan. Memulai dengan data kosong.")

    return stok_dict

# -----------------------------
# Fungsi: Menyimpan data ke file
# -----------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    """
    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")

# -----------------------------
# Fungsi: Menampilkan semua data
# -----------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    print("\n=== DAFTAR STOK BARANG ===")
    
    # TODO: Jika kosong, tampilkan pesan stok kosong
    if not stok_dict:
        print("Data stok kosong.")
        return

    # TODO: Tampilkan dengan format rapi
    print(f"{'KODE':<10} | {'NAMA BARANG':<15} | {'STOK':>5}")
    print("-" * 36)
    
    for kode in sorted(stok_dict.keys()):
        data = stok_dict[kode]
        print(f"{kode:<10} | {data['nama']:<15} | {data['stok']:>5}")

# -----------------------------
# Fungsi: Cari barang berdasarkan kode
# -----------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()

    # TODO: Cek apakah kode ada di dictionary
    if kode in stok_dict:
        data = stok_dict[kode]
        print("\n--- Barang Ditemukan ---")
        print(f"Kode  : {kode}")
        print(f"Nama  : {data['nama']}")
        print(f"Stok  : {data['stok']}")
    else:
        print("Barang tidak ditemukan.")

# -----------------------------
# Fungsi: Tambah barang baru
# -----------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    
    # TODO: Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print(f"Gagal: Kode '{kode}' sudah digunakan oleh {stok_dict[kode]['nama']}.")
        return

    nama = input("Masukkan nama barang: ").strip()
    
    # TODO: Input stok awal (integer)
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Input stok harus berupa angka.")
        return

    # TODO: Simpan ke dictionary
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print(f"Barang '{nama}' berhasil ditambahkan ke memori sementara.")

# -----------------------------
# Fungsi: Update stok barang
# -----------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # TODO: Cek apakah kode ada di dictionary
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print(f"Stok saat ini ({stok_dict[kode]['nama']}): {stok_dict[kode]['stok']}")
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # TODO: Input jumlah perubahan stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    # TODO: Logika update stok
    stok_sekarang = stok_dict[kode]["stok"]
    
    if pilihan == "1":
        stok_baru = stok_sekarang + jumlah
        stok_dict[kode]["stok"] = stok_baru
        print(f"Berhasil! Stok bertambah menjadi {stok_baru}.")
        
    elif pilihan == "2":
        stok_baru = stok_sekarang - jumlah
        # Cek hasil < 0
        if stok_baru < 0:
            print("Gagal: Stok tidak boleh negatif (kurang dari 0).")
        else:
            stok_dict[kode]["stok"] = stok_baru
            print(f"Berhasil! Stok berkurang menjadi {stok_baru}.")
    else:
        print("Pilihan tidak valid.")

# -----------------------------
# Program Utama
# -----------------------------
def main():
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan ke file.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()