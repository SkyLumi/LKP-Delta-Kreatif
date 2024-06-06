from connectDatabase import database as db
from tabulate import tabulate
import readController as rc
import BahanMentah as bm
import time
import fiturSearch as search
import os

conn = db()
cur = conn.cursor()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def selectIDPelatih(id_pelatih):
    query = f"""select id_pelatih, nama_pelatih, kontak_pelatih, provinsi ||', '||kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat
                from pelatih
                where id_pelatih = {id_pelatih}"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def selectByIDAdmin(id_admin):
    query = f"""select id_admin, nama_admin, nomor_telepon, provinsi ||', '||kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat
                from admin
                where id_admin = {id_admin}"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def checkIdAdminByUsername(username):
    query = f"""select id_admin
                from admin
                where username = '{username}'"""
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i

def addClass():
    while True:
        nama_kelas = input("Masukkan nama kelas baru: ")
        if nama_kelas == 'exit':
            break
        
        rc.viewPelatih()
        
        try:
            id_pelatih_input = input("Masukkan nama pelatih yang akan mengajar: ")
            if id_pelatih_input == 'exit':
                break
            id_pelatih = int(id_pelatih_input)
            
            selectIDPelatih(id_pelatih)
            
            choice = input("Apakah ingin menginput pelatih ini (y/n): ")
            if choice == 'exit':
                break
            elif choice != 'y' or '':
                continue

            rc.viewAdmin()
            
            id_admin_input = input("Masukkan admin yang akan mengelola kelas: ")
            if id_admin_input == 'exit':
                break
            id_admin = int(id_admin_input)

            selectByIDAdmin(id_admin_input)

            choice = input("Apakah ingin menginput pelatih ini (y/n): ")
            if choice == 'exit':
                break
            elif choice != 'y' or '':
                continue

            rc.viewJenisKelas()

            id_jenis_kelas_input = input("Masukkan jenis kelas: ")
            if id_jenis_kelas_input == 'exit':
                break
            id_jenis_kelas = int(id_jenis_kelas_input)
            
            
            
        except ValueError:
            print('Yang diinputkan harus berupa angka ya')
            continue
        
        waktu = input("Masukkan waktu: ")
        if waktu == 'exit':
            break
        
        hari = input("Masukkan hari: ")
        if hari == 'exit':
            break
        
        query = "INSERT INTO kelas (nama_kelas, id_pelatih, id_admin, id_jenis_kelas, waktu, hari) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (nama_kelas, id_pelatih, id_admin, id_jenis_kelas, waktu, hari))
        conn.commit()
        print("Kelas baru telah ditambahkan.")
        
        time.sleep(2)
        clear()
        break

def addPelatih():
    while True:
        try:
            nama_pelatih = input("Masukkan nama pelatih: ")
            if nama_pelatih == 'exit':
                break

            kontak_pelatih_input = input("Masukkan kontak pelatih: ")
            if kontak_pelatih_input == 'exit':
                break
            kontak_pelatih = int(kontak_pelatih_input)

            username = input("Masukkan username: ")
            if username == 'exit':
                break

            password = input("Masukkan password: ")
            if password == 'exit':
                break

            provinsi = input("Masukkan provinsi: ")
            if provinsi == 'exit':
                break

            kabupaten = input("Masukkan kabupaten: ")
            if kabupaten == 'exit':
                break

            kecamatan = input("Masukkan kecamatan: ")
            if kecamatan == 'exit':
                break

            jalan = input("Masukkan jalan: ")
            if jalan == 'exit':
                break

            query = """
                INSERT INTO pelatih (nama_pelatih, kontak_pelatih, username, password, provinsi, kabupaten, kecamatan, jalan)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (nama_pelatih, kontak_pelatih, username, password, provinsi, kabupaten, kecamatan, jalan))
            conn.commit()
            print("Pelatih baru telah ditambahkan.")
            time.sleep(2)
            break

        except ValueError:
            print('Kontak pelatih harus berupa angka.')
            continue

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            conn.rollback()

def homepageAdmin(username):
    while True:
        clear()
        print(f"Halo, {username}! Selamat datang di LKP Delta Kreatif")
        print("1. Lihat siswa")
        print("2. Lihat kelas")
        print("3. Tambah kelas")
        print("4. Tambah pelatih")
        print("5. Input bahan mentah")
        print("6. Lihat bahan mentah")
        print("7. Lihat Pelatih")
        print("8. Logout")
        
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            clear()
            rc.viewStudents()
            print('search siswa')
            search.searchSiswa()
        elif choice == '2':
            clear()
            rc.viewkelas()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '3':
            clear()
            addClass()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '4':
            clear()
            addPelatih()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '5':
            clear()
            id_admin = checkIdAdminByUsername(username)
            bm.addBahanMentah(id_admin)
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '6':
            clear()
            rc.viewBahanMentah()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '7':
            clear()
            rc.viewPelatih()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '8':
            clear()
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")