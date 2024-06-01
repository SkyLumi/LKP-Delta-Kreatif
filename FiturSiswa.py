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
    query = "SELECT nama_kelas, jk.nama_jenis_kelas, jk.deskripsi, hari, waktu FROM kelas k join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas"
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
        pemilihanKelas()

