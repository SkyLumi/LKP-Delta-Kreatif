import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def fetchKelasSiswa(username):
    query = """
        SELECT id_kelas, nama_kelas, nama_pelatih, hari, waktu 
        FROM siswa s
        JOIN classes c ON s.id_kelas = c.class_id
        WHERE s.username = %s
    """
    cur.execute(query, (username,))
    result = cur.fetchone()
    return result[0] if result else None

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

def homepageSiswa(username):
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
            else:
                print("Pemilihan kelas dibatalkan.")
        except ValueError:
            print('harus berupa angka ya')
    else:
        print('jadwal')
