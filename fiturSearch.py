from connectDatabase import database as db
from tabulate import tabulate
from clear import clear

conn = db()
cur = conn.cursor()

def searchSiswa():    
    while True:
        search_query = input("Masukkan nama siswa atau 'exit' untuk keluar: ")
        if search_query.lower() == 'exit':
            break

        clear()

        try:
            query = """select id_siswa, nama_siswa, tanggal_lahir, gender_siswa, username, provinsi ||', '|| kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat, k.nama_kelas ||', '|| jk.nama_jenis_kelas as kelas_siswa 
                from siswa s
                join kelas k on s.id_kelas = k.id_kelas
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas WHERE nama_siswa ILIKE %s order by id_siswa asc"""
            cur.execute(query, (f"%{search_query}%",))
            data = cur.fetchall()
    
            if data:
                colnames = [desc[0] for desc in cur.description]
                print(tabulate(data, headers=colnames, tablefmt="grid"))
            else:
                print("Tidak ada data siswa yang ditemukan.")
        
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def searchPelatih():
    while True:
        search_query = input("Masukkan nama pelatih atau 'exit' untuk keluar: ")
        if search_query.lower() == 'exit':
            break
        
        try:
            query = "SELECT id_pelatih, nama_pelatih, kontak_pelatih, username, provinsi, kabupaten, kecamatan, jalan FROM pelatih WHERE nama_pelatih ILIKE %s"
            cur.execute(query, (f"%{search_query}%",))
            rows = cur.fetchall()
            
            if rows:
                for row in rows:
                    print(f"ID Pelatih: {row[0]}, Nama Pelatih: {row[1]}, Kontak Pelatih: {row[2]}, Username: {row[3]}, Provinsi: {row[4]}, Kabupaten: {row[5]}, Kecamatan: {row[6]}, Jalan: {row[7]}")
            else:
                print("Tidak ada pelatih yang ditemukan dengan nama tersebut.")
        
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")