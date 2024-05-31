import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def Login():
    while True:
        username = input('Username: ')
        password = input('Password: ')
        
        query = "SELECT username, password FROM admin WHERE username = %s"
        cur.execute(query, (username,))
        data = cur.fetchone()
        
        if data and data[1] == password:
            homepageSiswa()
            break
        else:
            print("Username atau password kamu ada yang salah sepertinya.")
            try_again = input("Coba lagi? (y/n): ").strip().lower()
            if try_again != 'y':
                break

def Register():
    nama_siswa = input("Enter Nama Siswa: ")
    umur_siswa = input("Enter Umur Siswa: (L / P)")
    gender_siswa = input("Enter Gender Siswa: ")
    bekerja_atau_sekolah = input("Enter Bekerja atau Sekolah y/n: ")

    if bekerja_atau_sekolah == 'y':
        bekerja_atau_sekolah = 1
    elif bekerja_atau_sekolah == 'n':
        bekerja_atau_sekolah = 0
    else:
        print('Inputanmu salah nih')

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    provinsi = input("Enter Provinsi: ")
    kabupaten = input("Enter Kabupaten: ")
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
                Login()
            case 2:
                Register()
            case 3:
                print("Keluar...")
                break
            case _:
                print("Ups, inputan kamu sepertinya salah.")

startup()

# Jangan lupa untuk menutup cursor dan koneksi setelah selesai
cur.close()
conn.close()
