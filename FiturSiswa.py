import psycopg2
from tabulate import tabulate
import time

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def cekIDSiswa(username):
    query = f"""
            select id_siswa
            from siswa
            where username == '{username}'"""
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i

def readPelatih(username):
    query = f"""
        select p.nama_pelatih, p.kontak_pelatih, p.kabupaten ||', '|| p.kecamatan ||', '|| p.jalan as Alamat
        FROM siswa s
        JOIN kelas k on s.id_kelas = k.id_kelas
        join pelatih p on k.id_pelatih = p.id_pelatih
        WHERE s.username = '{username}'
    """
    cur.execute(query)

    data = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    print(tabulate(data, headers=colnames, tablefmt='grid'))

def fetchJadwalKelasSiswa(username):
    query = f"""
        SELECT k.nama_kelas, k.hari, k.waktu 
        FROM siswa s
        JOIN kelas k on s.id_kelas = k.id_kelas
        join pelatih p on k.id_pelatih = p.id_pelatih
        WHERE s.username = '{username}'
    """
    cur.execute(query)

    data = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    print(tabulate(data, headers=colnames, tablefmt='grid'))

def fetchNamaSiswa(username):
    query = f"SELECT nama_siswa FROM siswa WHERE username = '{username}'"
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i
    
def cekKelasSiswa(username):
    query = f"SELECT id_kelas FROM siswa WHERE username = '{username}'"
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i
    
def updateKelasSiswa(username, kelas_id):
    cur.execute("UPDATE siswa SET id_kelas = %s WHERE username = %s", (kelas_id, username))
    conn.commit()


def cekKelas(id_kelas):
    query = f"""SELECT id_kelas, nama_kelas, nama_pelatih, hari, waktu 
                FROM kelas k
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas 
                join pelatih p on k.id_pelatih = p.id_pelatih 
                WHERE id_kelas = '{id_kelas}'"""
    cur.execute(query)
    data = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    print(tabulate(data, headers=colnames, tablefmt='grid'))

def cekKelasMore(username):
    query = f"""
        SELECT k.nama_kelas, jk.jenis_kelas, jk.deskripsi
        FROM siswa s
        JOIN kelas k on s.id_kelas = k.id_kelas
        join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas
        WHERE s.username = '{username}'
    """
    cur.execute(query)
    data = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    print(tabulate(data, headers=colnames, tablefmt='grid'))

def pemilihanKelas():
    query = """SELECT id_kelas, nama_kelas, p.nama_pelatih, hari, waktu 
                FROM kelas k 
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas 
                join pelatih p on k.id_pelatih = p.id_pelatih"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")
        
def cekSertifikat(id_siswa):
    query = f"SELECT id_siswa FROM siswa WHERE id_siswa = '{id_siswa}'"
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i

def homepageSiswa(username):
    while True:
        nama = fetchNamaSiswa(username)
        print(f"Halo {nama}, selamat datang!")
        kelas = cekKelasSiswa(username)
        if kelas == None:
            print('Silahkan pilih kelas dulu ya')
            pemilihanKelas()
            try:
                kelas = int(input('masukkan nama kelasnya: '))
                cekKelas(kelas)
                confirm = input('Yakin memilih ini? (y/n): ')
                if confirm == 'y':
                    updateKelasSiswa(username, kelas)
                    print("Kelas telah dipilih.")
                    print('Kamu dapat keluar sekarang')
                    input('Kamu dapat melihat jadwal kembali jika login')
                else:
                    print("Pemilihan kelas dibatalkan.")
            except ValueError:
                print('harus berupa angka ya')
        else:
            print('\nJadwal kamu, jangan lupa yaa\n')
            fetchJadwalKelasSiswa(username)
            print("\nmenu:\n")
            print("1. informasi pelatih: ")
            print("2. informasi kelas")
            print("3. cek sertifikat")
            try:
                choice = int(input("\nsilahkan pilih:  "))
                match choice:
                    case 1:
                        readPelatih(username)
                        input("Enter untuk kembali...")
                        continue
                    case 2:
                        cekKelasMore(username)
                        input("Enter untuk kembali...")
                        continue
                    case 3:
                        id_siswa = cekIDSiswa(username)
                        cekSertifikat(id_siswa)
            except ValueError:
                print('harus angka yah')
                time.sleep(2)
                continue