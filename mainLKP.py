import FiturAdmin as Fa
import FiturPelatih as Fp
import FiturSiswa as Fs
import psycopg2
import Design as ui
from tabulate import tabulate
import os
import time

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_credentials(table, username, password):
    query = f"SELECT username, password FROM {table} WHERE username = %s"
    cur.execute(query, (username,))
    data = cur.fetchone()
    return data and data[1] == password

def username_exists(username):
    query = "SELECT 1 FROM admin WHERE username = %s UNION SELECT 1 FROM pelatih WHERE username = %s UNION SELECT 1 FROM siswa WHERE username = %s"
    cur.execute(query, (username, username, username))
    return cur.fetchone() is not None

def Login():
    while True:
        username = input('Username: ')
        password = input('Password: ')
        
        if check_credentials('admin', username, password):
            clear()
            Fa.homepageAdmin(username)
            break
        elif check_credentials('pelatih', username, password):
            clear()
            Fp.homepagePelatih()
            break
        elif check_credentials('siswa', username, password):
            clear()
            Fs.homepageSiswa(username)
            break
        else:
            print("Username atau password kamu ada yang salah sepertinya.")
            try_again = input("Coba lagi? (y/n): ").strip().lower()
            if try_again != 'y' or '':
                clear()
                break
            else:
                clear()


def Register():
    while True:
        ui.logoDeltaKreatif()
        nama_siswa = input("Enter Nama Siswa: ")
        
        try:
            umur_siswa = int(input("Enter Umur Siswa: "))
        except ValueError:
            print("Umur harus berupa angka.")
            time.sleep(2)
            clear()
            continue
        
        gender_siswa = input("Enter Gender Siswa (L / P): ")
        if gender_siswa not in ['L', 'P']:
            print("Inputan gender kamu ada yang salah nih.")
            time.sleep(2)
            clear()
            continue
        
        bekerja_atau_sekolah = input("Enter Bekerja atau Sekolah (y/n): ")
        if bekerja_atau_sekolah == 'y':
            print('maaf kamu tidak memenuhi persyaratan untuk ikut pelatihan ini')
            time.sleep(2)
            clear()
            continue
        elif bekerja_atau_sekolah == 'n':
            print('kamu memenuhi persyaratan LKP Delta Kreatif')
        else:
            print('Inputan bekerja atau sekolah kamu ada yang salah nih.')
            time.sleep(2)
            clear()
            continue

        username = input("Enter Username: ")
        if username_exists(username):
            print("Username sudah ada, silakan pilih username lain.")
            time.sleep(2)
            clear()
            continue
        password = input("Enter Password: ")
        provinsi = input("Enter Provinsi: ")
        kabupaten = input("Enter Kabupaten: ")

        if provinsi != 'Jawa Timur' or kabupaten != 'Bondowoso':
            print('Maaf, kita hanya menerima di area Bondowoso.')
            time.sleep(2)
            clear()
            continue
        
        kecamatan = input("Enter Kecamatan: ")
        jalan = input("Enter Jalan: ")

        query = """
            INSERT INTO siswa (
                nama_siswa, umur_siswa, gender_siswa, username, password, provinsi, kabupaten, kecamatan, jalan
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (nama_siswa, umur_siswa, gender_siswa, username, password, provinsi, kabupaten, kecamatan, jalan))
        conn.commit()

        print("Data mu sudah terupload.")
        print("Silahkan login kembali.")
        time.sleep(2)
        clear()
        break

def startup():
    while True:
        ui.logoDeltaKreatif()
        print("Selamat Datang di LKP Delta Kreatif:\n")
        print("1. Login\n"
              "2. Register\n"
              "3. Exit\n")
        pilihan = int(input("Silahkan dipilih: "))
        match pilihan:
            case 1:
                clear()
                ui.logoDeltaKreatif()
                Login()
            case 2:
                clear()
                Register()
            case 3:
                print("Keluar...")
                time.sleep(2)
                clear()
                break
            case _:
                ui.logoDeltaKreatif()
                print("Ups, inputan kamu sepertinya salah.")
                time.sleep(1)
                clear()
clear()
startup()

cur.close()
conn.close()
