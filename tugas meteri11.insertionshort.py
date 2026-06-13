# ============================================================
#   PROGRAM PERINGKAT NILAI SISWA
#   Algoritma: Bubble Sort & Insertion Sort (Descending)
# ============================================================
 
# --- DATA SISWA ---
# Format: dictionary dengan nama sebagai key, nilai sebagai value
data_siswa = {
    "Andi":   78,
    "Budi":   92,
    "Citra":  85,
    "Dewi":   70,
    "Eka":    95,
    "Fajar":  88,
    "Gita":   60,
    "Hendra": 75,
}
 
 
# ============================================================
# FUNGSI HELPER
# ============================================================
 
def tampilkan_data(data, judul="Data Siswa"):
    """Menampilkan data siswa dalam format tabel."""
    print(f"\n{'='*40}")
    print(f"  {judul}")
    print(f"{'='*40}")
    print(f"  {'No':<5} {'Nama':<12} {'Nilai':<8} {'Peringkat'}")
    print(f"  {'-'*35}")
    for i, (nama, nilai) in enumerate(data, start=1):
        bintang = "★" * (nilai // 20)  # bintang sebagai indikator visual
        print(f"  {i:<5} {nama:<12} {nilai:<8} {bintang}")
    print(f"{'='*40}\n")
 
 
def konversi_ke_list(dict_siswa):
    """Mengubah dictionary menjadi list of tuple [(nama, nilai), ...]."""
    return list(dict_siswa.items())
 
 
# ============================================================
# 1. BUBBLE SORT (Descending / Tertinggi ke Terendah)
# ============================================================
 
def bubble_sort(data):
    """
    Bubble Sort — membandingkan dua elemen berdekatan, lalu tukar
    jika elemen kiri LEBIH KECIL dari elemen kanan.
    Ulangi sampai tidak ada pertukaran (data sudah terurut).
    
    Kompleksitas waktu: O(n²)
    """
    # Salin data agar data asli tidak berubah
    arr = data[:]
    n = len(arr)
 
    print("\n[BUBBLE SORT] Proses pengurutan:")
    print(f"  Data awal: {[f'{nama}({nilai})' for nama, nilai in arr]}")
 
    for i in range(n - 1):          # Iterasi luar: n-1 putaran
        ada_pertukaran = False
 
        for j in range(n - 1 - i):  # Iterasi dalam: semakin mengecil
            nama_kiri,  nilai_kiri  = arr[j]
            nama_kanan, nilai_kanan = arr[j + 1]
 
            # Tukar jika nilai kiri LEBIH KECIL (karena kita mau descending)
            if nilai_kiri < nilai_kanan:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ada_pertukaran = True
 
        # Tampilkan kondisi setelah setiap putaran
        urutan = [f"{nama}({nilai})" for nama, nilai in arr]
        print(f"  Putaran {i+1}: {urutan}")
 
        # Optimasi: berhenti lebih awal jika tidak ada pertukaran
        if not ada_pertukaran:
            print(f"  → Tidak ada pertukaran, pengurutan selesai lebih awal!")
            break
 
    return arr
 
 
# ============================================================
# 2. INSERTION SORT (Descending / Tertinggi ke Terendah)
# ============================================================
 
def insertion_sort(data):
    """
    Insertion Sort — ambil satu elemen dari kanan, lalu sisipkan
    ke posisi yang tepat di bagian kiri yang sudah terurut.
    
    Analogi: seperti ngurutin kartu di tangan satu per satu.
    
    Kompleksitas waktu: O(n²)
    """
    # Salin data agar data asli tidak berubah
    arr = data[:]
    n = len(arr)
 
    print("\n[INSERTION SORT] Proses pengurutan:")
    print(f"  Data awal: {[f'{nama}({nilai})' for nama, nilai in arr]}")
 
    for i in range(1, n):           # Mulai dari elemen ke-2
        kunci = arr[i]              # Elemen yang akan disisipkan
        j = i - 1
 
        # Geser elemen yang lebih kecil dari kunci ke kanan
        while j >= 0 and arr[j][1] < kunci[1]:
            arr[j + 1] = arr[j]
            j -= 1
 
        # Sisipkan kunci ke posisi yang tepat
        arr[j + 1] = kunci
 
        # Tampilkan kondisi setelah setiap sisipan
        urutan = [f"{nama}({nilai})" for nama, nilai in arr]
        print(f"  Sisip '{kunci[0]}({kunci[1]})' → {urutan}")
 
    return arr
 
 
# ============================================================
# PROGRAM UTAMA
# ============================================================
 
if __name__ == "__main__":
 
    print("\n" + "★"*50)
    print("   SISTEM PERINGKAT NILAI SISWA")
    print("   Algoritma Sorting — Python")
    print("★"*50)
 
    # Tampilkan data awal (belum diurutkan)
    data_list = konversi_ke_list(data_siswa)
    tampilkan_data(data_list, judul="DATA AWAL (Belum Diurutkan)")
 
    # ---- Pilih algoritma ----
    print("Pilih algoritma sorting:")
    print("  1. Bubble Sort")
    print("  2. Insertion Sort")
    print("  3. Tampilkan keduanya")
    pilihan = input("\nMasukkan pilihan (1/2/3): ").strip()
 
    if pilihan == "1":
        hasil = bubble_sort(data_list)
        tampilkan_data(hasil, judul="HASIL PERINGKAT (Bubble Sort)")
 
    elif pilihan == "2":
        hasil = insertion_sort(data_list)
        tampilkan_data(hasil, judul="HASIL PERINGKAT (Insertion Sort)")
 
    elif pilihan == "3":
        hasil_bubble    = bubble_sort(data_list)
        hasil_insertion = insertion_sort(data_list)
 
        tampilkan_data(hasil_bubble,    judul="HASIL PERINGKAT (Bubble Sort)")
        tampilkan_data(hasil_insertion, judul="HASIL PERINGKAT (Insertion Sort)")
 
        # Verifikasi: kedua algoritma harus menghasilkan hasil yang sama
        print("Verifikasi: Hasil kedua algoritma sama?", 
              "✓ YA" if hasil_bubble == hasil_insertion else "✗ TIDAK")
    else:
        print("Pilihan tidak valid. Menjalankan Bubble Sort secara default...")
        hasil = bubble_sort(data_list)
        tampilkan_data(hasil, judul="HASIL PERINGKAT (Bubble Sort)")
 
    print("Program selesai. Terima kasih!\n")
 