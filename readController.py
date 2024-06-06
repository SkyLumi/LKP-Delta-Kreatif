from connectDatabase import database as db
from tabulate import tabulate
import time
import os

conn = db()

cur = conn.cursor()

def viewPelatih():
    query = """select id_pelatih, nama_pelatih, kontak_pelatih, provinsi ||', '||kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat
                from pelatih
                limit 5"""
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
    query = """select id_siswa, nama_siswa, tanggal_lahir, gender_siswa, username, provinsi ||', '|| kabupaten ||', '|| kecamatan ||', '|| jalan as Alamat, k.nama_kelas ||', '|| jk.nama_jenis_kelas as kelas_siswa 
                from siswa s
                join kelas k on s.id_kelas = k.id_kelas
                join jenis_kelas jk on k.id_jenis_kelas = jk.id_jenis_kelas
                order by id_siswa asc
                limit 5"""
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

def viewJenisKelas():
    query = """SELECT id_jenis_kelas, nama_jenis_kelas, deskripsi
                FROM jenis_kelas 
                """
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data kelas yang ditemukan.")

def viewBahanMentah():
    query = """SELECT bm.id_bahan_mentah, 
                bm.nama_bahan_mentah, 
                bm.kuantitas_bahan_mentah, 
                sb.nama_satuan_bahan_mentah, 
                jb.nama_jenis_bahan_mentah, 
                p.nama_pelatih AS "diambil oleh", 
                a.nama_admin AS "diinput oleh"
                FROM bahan_mentah bm
                JOIN jenis_bahan_mentah jb ON bm.id_jenis_bahan_mentah = jb.id_jenis_bahan_mentah
                JOIN satuan_bahan_mentah sb ON bm.id_satuan_bahan_mentah = sb.id_satuan_bahan_mentah
                LEFT JOIN pelatih p ON bm.id_pelatih = p.id_pelatih
                JOIN admin a ON bm.id_admin = a.id_admin;
                """
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data kelas yang ditemukan.")

def viewJenisBahanMentah():
    query = """SELECT *
                FROM jenis_bahan_mentah
                """
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data jenis bahan yang ditemukan.")

def viewSatuanBahanMentah():
    query = """SELECT *
                FROM satuan_bahan_mentah
                """
    cur.execute(query)
    data = cur.fetchall()
    
    if data:
        colnames = [desc[0] for desc in cur.description]
        print(tabulate(data, headers=colnames, tablefmt="grid"))
    else:
        print("Tidak ada data satuan bahan yang ditemukan.")