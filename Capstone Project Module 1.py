import random  
import time

# Data Barang
list_nama = [
    "Walls Magnum Belgian Chocolate",
    "Frisian Flag UHT Coklat 1L",
    "Air Mineral Aqua Galon 19L",
    "Jamu Tolak Angin 5x15 ml",
    "Nestle Koko Krunch 300gm"
] # Nama Barang
list_harga = [15000, 15500, 19500, 20200, 43700]  # Harga Barang
list_terjual = []  # Barang Terjual
list_laba = []  # Laba
list_stok = []  # Stok
max_stok = 200  # Stok Maximum

def generate_penjualan(list_nama): # Membuat Data Penjualan
    list_terjual = []  
    for i in range(len(list_nama)):  
        terjual = random.randint(1, 200)  
        list_terjual.append(terjual) 
    return list_terjual

def hitung_laba(list_harga, list_terjual): # Menghitung Laba
    list_laba = []  
    for i in range(len(list_harga)):  
        laba = list_harga[i] * list_terjual[i]  
        list_laba.append(laba)  
    return list_laba  

def hitung_stok(list_terjual): # Menghitung Stok
    list_stok = []  
    for i in range(len(list_terjual)):  
        stok = max_stok - list_terjual[i]  
        list_stok.append(stok)  
    return list_stok  

def tunggu_user(): # untuk menunggu sampai user selesai
    user_input2 = input("Tekan apapun untuk melanjutkan...")
    time.sleep(0.5)

def check_batal(prompt): # Jika user tidak jadi update data
    try:
        user_input = input(prompt)  
        return int(user_input)  
    except ValueError:
        print("Membatalkan...")
        return None
    
def tambah_barang_baru(list_terjual, list_stok, list_laba, max_stok): # Menambahkan Barang Baru
    
    print("\n===== Tambah Barang Baru =====")
    nama_baru = input("Masukkan Nama Barang: ")
    while True:
        time.sleep(0.5)
        try:
            harga_baru = int(input("Masukkan Harga Barang: "))
            if harga_baru > 100:
                break
            else:
                print("Harga harus lebih dari 100 Perak!")
        except ValueError:
            print("Harga harus dalam angka bulat!")

    while True:
        stok_baru = int(input(f"Masukkan Stok Barang (1-{max_stok}): "))
        if 1 <= stok_baru <= max_stok:
            break
        else:
            print(f"Stok harus diantara 1 dan {max_stok}!")
    
    time.sleep(0.5)

    print(f"""\n=== Konfirmasi Data Barang ===\nNama Barang : {nama_baru:<15}\nHarga Barang: Rp.{harga_baru:<15,}\nStok Barang : {stok_baru:<15}""")

    confirm = input("\nApakah Anda yakin ingin menambahkan barang ini? (Y untuk ya, N untuk batal): ")

    if confirm.upper() == "Y":  
        list_nama.append(nama_baru)
        list_harga.append(harga_baru)
        list_terjual.append(0)
        list_stok.append(stok_baru)
        list_laba.append(0)
        print(f"Barang '{nama_baru}' berhasil ditambahkan!")
    else:
        print("Penambahan barang dibatalkan.")

    time.sleep(0.5)

def hapus_barang(list_terjual, list_stok, list_laba): # Untuk me-delete barang

    print("\n===== Hapus Data Barang =====")
    for i in range(len(list_nama)):
        print(f"{i + 1}. {list_nama[i]}")  
    
    while True:
        barang_hapus = check_batal("Masukkan nomor barang yang ingin dihapus (input huruf untuk batal): ")
        if barang_hapus is None:  
            print("Penghapusan barang dibatalkan.")
            break

        barang_hapus -= 1  

        if 0 <= barang_hapus < len(list_nama):  
            print(f"Barang '{list_nama[barang_hapus]}' telah dihapus!")
            list_nama.pop(barang_hapus)
            list_harga.pop(barang_hapus)
            list_terjual.pop(barang_hapus)
            list_stok.pop(barang_hapus)
            list_laba.pop(barang_hapus)
            break  
        else:
            print("Barang Ini tidak Ada!")

def update_barang(list_terjual, list_stok, list_laba, max_stok): # Untuk semua proses update dan modifikasi data barang

    print("\n===== Update Data Barang =====")
    for i in range(len(list_nama)):
        print(f"{i + 1}. {list_nama[i]}")  

    while True:
        barang_update = check_batal("\nMasukkan nomor barang yang ingin di-update (input huruf untuk batal): ")
        if barang_update is None:  
            print("Update data barang dibatalkan.")
            break  

        barang_update -= 1 

        if 0 <= barang_update < len(list_nama):  
            while True:  
                print("\nApa yang ingin Anda update?\n"
                      "1. Harga Barang\n"
                      "2. Stok Barang\n"
                      "3. Terjual\n"
                      "4. Kembali ke Menu Utama")
                pilihan_update = input("\nPilihan Anda: ")

                if pilihan_update == "1":
                    harga_update = check_batal("Masukkan Harga Baru (input huruf untuk batal): ")
                    if harga_update is None:
                        print("Update harga dibatalkan.")
                    elif harga_update <= 0:  
                        print("Harga barang harus lebih besar dari 0!")
                    else:
                        list_harga[barang_update] = harga_update
                        print("Harga berhasil diupdate!")
                
                elif pilihan_update == "2":
                    while True:
                        stok_baru = check_batal(f"Masukkan Stok Baru (1-{max_stok}) (input huruf untuk batal): ")
                        if stok_baru is None:
                            print("Update stok dibatalkan.")
                            break  
                        elif 1 <= stok_baru <= max_stok:
                            list_stok[barang_update] = stok_baru
                            print("Stok berhasil diupdate!")
                            break  
                        else:
                            print(f"Stok harus antara 1 dan {max_stok}. Silakan coba lagi!")

                elif pilihan_update == "3":
                    try:
                        terjual_update = check_batal("Masukkan Jumlah Barang Terjual (input huruf untuk batal): ")
                        if terjual_update is None:
                            print("\nUpdate penjualan dibatalkan.")
                            break
                        if terjual_update < 0:  
                            print("Jumlah terjual tidak bisa negatif!")
                        elif terjual_update > list_stok[barang_update]:  
                            time.sleep(0.5)
                            print(f"\nJumlah stok tidak cukup! sisa stok {list_nama[barang_update]} saat ini: ({list_stok[barang_update]})")
                            time.sleep(1)
                        else:
                            list_terjual[barang_update] = terjual_update
                            list_stok[barang_update] -= terjual_update  
                            list_laba[barang_update] = list_harga[barang_update] * terjual_update
                            time.sleep(0.5)
                            print("Data penjualan berhasil diupdate!")
                            time.sleep(0.5)
                            print(f"\nStok tersisa untuk {list_nama[barang_update]}: {list_stok[barang_update]}")
                    except ValueError:
                        print("Input tidak valid! Update dibatalkan.")

                elif pilihan_update == "4":
                    print("Kembali ke Menu Utama...")
                    break  

                else:
                    print("Pilihan ini tidak valid!")
            
            break 
        else:
            print("Barang ini tidak ada!")

def menu_tampilkan(list_terjual, list_laba, list_stok): # Menu menampilkan data barang di list
    while True:
        time.sleep(0.5)
        print("\n===== Menu Menampilkan Data =====\n"
              "1. Data Inventori\n"
              "2. Data Penjualan \n"
              "3. Total Laba\n"
              "4. Kembali ke Menu Utama")
        
        user_input1 = input("\nData apa yang ingin di lihat?: ")
        time.sleep(0.5)

        if user_input1 == "1":
            print("\n===== Data Inventori =====")
            print(f"{'Nama Barang':<40}{'Harga':<10}{'Stok':<10}")
            print("-" * 65)
            for i in range(len(list_nama)):
                print(f"{list_nama[i]:<40}Rp.{list_harga[i]:<10,}{list_stok[i]:<10}")
            print("-" * 65)
            tunggu_user()
        elif user_input1 == "2":
            print("\n===== Data Penjualan =====")
            print(f"{'Nama Barang':<40}{'Harga':<10}{'Terjual':<10}{'Laba':<15}")
            print("-" * 65)
            for i in range(len(list_nama)):
                print(f"{list_nama[i]:<40}Rp.{list_harga[i]:<10,}{list_terjual[i]:<10}Rp.{list_laba[i]:<15,}")
            print("-" * 65)
            tunggu_user()
        elif user_input1 == "3":
            total_laba = sum(list_laba)
            print("\n===== Total Laba =====")
            print(f"Total Laba: Rp.{total_laba:<15,}")
            print("-" * 65)
            tunggu_user()
        elif user_input1 == "4":
            print("Kembali ke Menu Utama...")
            time.sleep(0.5)
            break
        else:
            print("Pilihan ini tidak ada di Menu!")
            time.sleep(0.5)

def menu_update(list_terjual, list_laba, list_stok): # Menu mengubah data barang di list
    while True:
        time.sleep(0.5)
        print("\n===== Menu Modifikasi Data =====\n"
              "1. Tambah Barang Baru\n"
              "2. Hapus Barang\n"
              "3. Update Data Barang (Kecuali Nama)\n"
              "4. Kembali ke Menu Utama")
        
        input_menu_update = input("\nApa yang ingin Anda Modifikasi?: ")
        time.sleep(0.5)

        if input_menu_update == "1":
            tambah_barang_baru(list_terjual, list_stok, list_laba, max_stok)
            
        elif input_menu_update == "2":
            hapus_barang(list_terjual, list_stok, list_laba)

        elif input_menu_update == "3":
            update_barang(list_terjual, list_stok, list_laba, max_stok)
        elif input_menu_update == "4":
            print("Kembali ke Menu Utama...")
            time.sleep(0.5)
            break
        else:
            print("Pilihan ini tidak ada di Menu!")
            time.sleep(0.5)

def main_menu():
    list_terjual = generate_penjualan(list_nama)  
    list_laba = hitung_laba(list_harga, list_terjual)  
    list_stok = hitung_stok(list_terjual)  
    
    while True:
        print("\n===== Sistem Manajemen Inventori dan Penjualan =====")
        print("\n1. Tampilkan Data"
              "\n2. Modifikasi Data"
              "\n3. Exit") 
        
        pilihan_user = input("\nMasukkan pilihan Anda: ")
        time.sleep(0.5)
        
        if pilihan_user == "1":
            menu_tampilkan(list_terjual, list_laba, list_stok)  
        elif pilihan_user == "2":
            menu_update(list_terjual, list_laba, list_stok) 
        elif pilihan_user == "3":
            print("Terimakasih. Sampai jumpa!")
            time.sleep(0.5)
            break
        else:
            print("Pilihan ini tidak ada di menu!")
            time.sleep(0.5)

main_menu()