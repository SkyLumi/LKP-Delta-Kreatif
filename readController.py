import psycopg2
from tabulate import tabulate
import time
import os

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

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


def viewStudents():
    query = """select id_siswa, nama_siswa, umur_siswa, gender_siswa, username, provinsi ||', '|| kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat, k.nama_kelas ||', '|| jk.nama_jenis_kelas as kelas_siswa 
                from siswa s
                join kelas k on s.id_kelas = k.id_kelas
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas
                order by id_siswa asc"""
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data siswa yang ditemukan.")

def viewkelas():
    query = """SELECT id_kelas, nama_kelas, p.nama_pelatih as Mengajar, a.nama_admin as Mengelola, jk.nama_jenis_kelas as Jenis 
                FROM kelas k
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas 
                join pelatih p on k.id_pelatih = p.id_pelatih
                join admin a on k.id_admin = a.id_admin"""
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data kelas yang ditemukan.")