import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def Login(username, password):
    query = f"select username from admin where username ilike '{username}'"
    cur.execute(query)
    data = cur.fetchall()
    

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
        print('inputanmu salah nih')

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    provinsi = input("Enter Provinsi: ")
    kabupaten = input("Enter Kabupaten: ")
    kecamatan = input("Enter Kecamatan: ")
    jalan = input("Enter Jalan: ")

    query = """
        INSERT INTO siswa (
            nama_siswa, umur_siswa, gender_siswa, bekerja_atau_sekolah, username, password, provinsi, kabupaten, kecamatan, jalan
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (nama_siswa, umur_siswa, gender_siswa, bekerja_atau_sekolah, username, password, provinsi, kabupaten, kecamatan, jalan))
    conn.commit()

    print("data mu sudah terupload.")

def homepageAdmin():
    print(f'Selamat Datang')

def readPelatih():
    query = "SELECT * FROM Pelatih"
    cur.execute(query)
    data = cur.fetchall()
    
    if data:

        colnames = [desc[0] for desc in cur.description]

        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def startup():
    while True:
        print("siapakah kamu? :")
        print("1. Login\n"
              "2. Register\n"
              "3. Exit\n")
        pilihan = int(input("silahkan di pilih: "))
        match pilihan:
            case 1:
                username = input('username : ')
                password = input('password : ')
                Login(username, password)
            case 2:
                Register()
            case 3:
                print("Keluar...")
                break
            case _:
                print("ups, Inputan kamu sepertinya salah.")

startup()

#kelas
#pelatih
#siswa
        