import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

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

def pemilihanKelas():
    query = """SELECT nama_kelas, p.nama_pelatih, hari, waktu 
                FROM kelas k 
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas 
                join pelatih p on k.id_pelatih = p.id_pelatih
                where jk.nama_jenis_kelas like 'Teori'"""
    cur.execute(query)
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def homepageSiswa(username):
    nama = fetchNamaSiswa(username)
    print(f"Halo {nama}, selamat datang!")
    kelas = cekKelasSiswa(username)
    if kelas == None:
        print('Silahkan pilih kelas dulu ya')
        pemilihanKelas()
        print('Setiap minggu diharuskan memiliki 4 pertemuan ()')
        try:
            input(int('Silahkan pilih kelas terlebih dahulu: '))
        except ValueError:
            print('harus berupa angka ya')
    else:
        print('jadwal')
