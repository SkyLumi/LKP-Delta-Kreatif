from connectDatabase import database as db
from tabulate import tabulate
import readController as rc
import fiturSearch as search
import BahanMentah as bm
import time
from clear import clear

conn = db()
cur = conn.cursor()

def updateJadwalKelas():
    while True:
        try:
            id_kelas = input("Masukkan ID Kelas yang ingin diupdate jadwalnya: ")
            if id_kelas == 'exit':
                break
            waktu_baru = input("Masukkan waktu baru (HH:MM): ")
            if id_kelas == 'exit':
                break
            hari_baru = input("Masukkan hari baru: ")
            if id_kelas == 'exit':
                break
            query = "UPDATE kelas SET waktu = %s, hari = %s WHERE id_kelas = %s;"
            cur.execute(query, (waktu_baru, hari_baru, id_kelas))
            conn.commit()
            print("Jadwal kelas telah diperbarui.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            conn.rollback()

def fetchJadwalKelasPelatih(username):
    query = f"""SELECT nama_kelas, hari, waktu 
                FROM kelas k
                join pelatih p on k.id_pelatih = p.id_pelatih
                WHERE p.username = '{username}'"""
    cur.execute(query)

    data = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    print(tabulate(data, headers=colnames, tablefmt='grid'))

def checkIdPelatihByUsername(username):
    query = f"""select id_pelatih
                from pelatih
                where username = '{username}'"""
    cur.execute(query)
    data = cur.fetchone()
    for i in data:
        return i


def homepagePelatih(username):
    while True:
        clear()
        print(f"selamat datang {username}, jadwal anda:")
        fetchJadwalKelasPelatih(username)
        print('1.melihat kelas')
        print('2.mengubah jadwal')
        print('3.mengambil bahan mentah')
        print('4.melihat bahan mentah')
        print('5.melihat siswa')
        print('6.logout')

        choice = input("Pilih opsi: ")
            
        if choice == '1':
            rc.viewkelas()
            input("Enter untuk berhenti melihat..")
        elif choice == '2':
            rc.viewkelas()
            updateJadwalKelas()
        elif choice == '3':
            rc.viewBahanMentah()
            bm.ambilBahanMentah(checkIdPelatihByUsername(username))
            input("Enter untuk berhenti melihat..")
        elif choice == '4':
            rc.viewBahanMentah()
            input("Enter untuk berhenti melihat..")
        elif choice == '5':
            rc.viewStudents()
            search.searchSiswa()
        elif choice == '6':
            print('selamat tinggal')
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        time.sleep(2)

    