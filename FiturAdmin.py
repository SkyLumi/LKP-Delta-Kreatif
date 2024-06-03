import psycopg2
from tabulate import tabulate
import time
import os

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def viewPelatih():
    query = """select id_pelatih, nama_pelatih, kontak_pelatih, provinsi ||', '||kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat
                from pelatih"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def viewAdmin():
    query = """select id_admin, nama_admin, nomor_telepon, provinsi ||', '||kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat
                from admin"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")
    
def selectIDPelatih(id_admin):
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

def viewStudents():
    query = """select id_siswa, nama_siswa, umur_siswa, gender_siswa, username, provinsi ||', '|| kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat, k.nama_kelas ||', '|| jk.nama_jenis_kelas as kelas_siswa 
                from siswa s
                join kelas k on s.id_kelas = k.id_kelas
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas"""
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data siswa yang ditemukan.")

def viewkelas():
    query = "SELECT * FROM kelas"
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data kelas yang ditemukan.")

def addClass():
    while True:
        nama_kelas = input("Masukkan nama kelas baru: ")
        if nama_kelas.lower() == 'exit':
            break
        
        viewPelatih()
        
        try:
            id_pelatih_input = input("Masukkan nama pelatih yang akan mengajar: ")
            if id_pelatih_input.lower() == 'exit':
                break
            id_pelatih = int(id_pelatih_input)
            
            selectIDPelatih(id_pelatih)
            
            choice = input("Apakah ingin menginput pelatih ini (y/n): ")
            if choice.lower() == 'exit':
                break
            if choice.lower() != 'y':
                continue

            viewAdmin()
            
            id_admin_input = input("Masukkan admin yang akan mengelola kelas: ")
            if id_admin_input.lower() == 'exit':
                break
            id_admin = int(id_admin_input)

            id_jenis_kelas_input = input("Masukkan jenis kelas: ")
            if id_jenis_kelas_input.lower() == 'exit':
                break
            id_jenis_kelas = int(id_jenis_kelas_input)
        
        except ValueError:
            print('Yang diinputkan harus berupa angka ya')
            continue
        
        waktu = input("Masukkan waktu kelas baru: ")
        if waktu.lower() == 'exit':
            break
        
        hari = input("Masukkan hari: ")
        if hari.lower() == 'exit':
            break
        
        query = "INSERT INTO kelas (nama_kelas, id_pelatih, id_admin, id_jenis_kelas, waktu, hari) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (nama_kelas, id_pelatih, id_admin, id_jenis_kelas, waktu, hari))
        conn.commit()
        print("Kelas baru telah ditambahkan.")
        
        time.sleep(2)
        clear()
        break


def removeClass():
    class_id = input("Masukkan ID kelas yang ingin dihapus: ")
    query = "DELETE FROM kelas WHERE class_id = %s"
    cur.execute(query, (class_id,))
    conn.commit()
    print("Kelas telah dihapus.")

def homepageAdmin(username):
    while True:
        clear()
        print(f"Halo, {username}! Selamat datang di LKP Delta Kreatif")
        print("1. Lihat siswa")
        print("2. Lihat kelas")
        print("3. Tambah kelas")
        print("4. Hapus kelas")
        print("5. Logout")
        
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            clear()
            viewStudents()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '2':
            clear()
            viewkelas()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '3':
            clear()
            addClass()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '4':
            clear()
            removeClass()
            input("Tekan Enter untuk melanjutkan...")
        elif choice == '5':
            clear()
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")