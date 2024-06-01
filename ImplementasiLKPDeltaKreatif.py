import FiturAdmin as Fa
import FiturPelatih as Fp
import psycopg2
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

def Login():
    while True:
        username = input('Username: ')
        password = input('Password: ')
        
        if check_credentials('admin', username, password):
            clear()
            Fa.homepageAdmin()
            break
        elif check_credentials('pelatih', username, password):
            clear()
            Fp.homepagePelatih()
            break
        elif check_credentials('siswa', username, password):
            clear()
            homepageSiswa()
            break
        else:
            print("Username atau password kamu ada yang salah sepertinya.")
            try_again = input("Coba lagi? (y/n): ").strip().lower()
            if try_again != 'y':
                clear()
                break
            else:
                clear()


def Register():
    while True:
        clear()
        nama_siswa = input("Enter Nama Siswa: ")
        
        try:
            umur_siswa = int(input("Enter Umur Siswa: "))
        except ValueError:
            print("Umur harus berupa angka.")
            continue
        
        gender_siswa = input("Enter Gender Siswa (L / P): ")
        if gender_siswa not in ['L', 'P']:
            print("Inputan gender kamu ada yang salah nih.")
            continue
        
        bekerja_atau_sekolah = input("Enter Bekerja atau Sekolah (y/n): ")
        if bekerja_atau_sekolah == 'y':
            bekerja_atau_sekolah = 1
        elif bekerja_atau_sekolah == 'n':
            bekerja_atau_sekolah = 0
        else:
            print('Inputan bekerja atau sekolah kamu ada yang salah nih.')
            continue

        username = input("Enter Username: ")
        password = input("Enter Password: ")
        provinsi = input("Enter Provinsi: ")
        kabupaten = input("Enter Kabupaten: ")

        if provinsi != 'Jawa Timur' or kabupaten != 'Bondowoso':
            print('Maaf, kita hanya menerima di area Bondowoso.')
            continue
        
        kecamatan = input("Enter Kecamatan: ")
        jalan = input("Enter Jalan: ")

        query = """
            INSERT INTO siswa (
                nama_siswa, umur_siswa, gender_siswa, bekerja_atau_sekolah, username, password, provinsi, kabupaten, kecamatan, jalan
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (nama_siswa, umur_siswa, gender_siswa, bekerja_atau_sekolah, username, password, provinsi, kabupaten, kecamatan, jalan))
        conn.commit()

        print("Data mu sudah terupload.")
        print("Silahkan login kembali.")
        time.sleep(2)
        clear()
        break

def homepageSiswa():
    print("Halo, selamat datang!")

def startup():
    while True:
        print("Selamat Datang di LKP Delta Kreatif:")
        print("1. Login\n"
              "2. Register\n"
              "3. Exit\n")
        pilihan = int(input("Silahkan dipilih: "))
        match pilihan:
            case 1:
                clear()
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
                print("Ups, inputan kamu sepertinya salah.")
                time.sleep(1)
                clear()
clear()
startup()

# Jangan lupa untuk menutup cursor dan koneksi setelah selesai
cur.close()
conn.close()
