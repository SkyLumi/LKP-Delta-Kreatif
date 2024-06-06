from tabulate import tabulate
from clear import clear
from connectDatabase import database as db
import readController as rc

conn = db()
cur = conn.cursor()

def addBahanMentah(id_admin):
    try:
        nama_bahan_mentah = input("Masukkan nama bahan mentah: ")
        rc.viewSatuanBahanMentah()
        id_satuan_bahan_mentah = int(input("Masukkan ID satuan bahan mentah: "))
        kuantitas_bahan_mentah = int(input("Masukkan kuantitas bahan mentah: "))
        rc.viewJenisBahanMentah()
        id_jenis_bahan_mentah = int(input("Masukkan ID jenis bahan mentah: "))

        query = """
            INSERT INTO bahan_mentah (nama_bahan_mentah, kuantitas_bahan_mentah, id_jenis_bahan_mentah, id_admin, id_satuan_bahan_mentah)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (nama_bahan_mentah, kuantitas_bahan_mentah, id_jenis_bahan_mentah, id_admin, id_satuan_bahan_mentah))
        conn.commit()
        print("Bahan mentah baru telah ditambahkan.")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        conn.rollback()

def ambilBahanMentah(id_pelatih):
    try:
        id_bahan_mentah = int(input("Masukkan ID bahan mentah yang ingin diambil: "))
        
        query_check = "SELECT id_pelatih FROM bahan_mentah WHERE id_bahan_mentah = %s;"
        cur.execute(query_check, (id_bahan_mentah,))
        result = cur.fetchone()
        
        if result:
            if result[0] is None:
                query_update = "UPDATE bahan_mentah SET id_pelatih = %s WHERE id_bahan_mentah = %s;"
                cur.execute(query_update, (id_pelatih, id_bahan_mentah))
                conn.commit()
                print("Bahan mentah berhasil diambil oleh pelatih.")
            else:
                print("Maaf, bahan mentah sudah diambil oleh pelatih lainnya.")
        else:
            print("ID bahan mentah tidak ditemukan.")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        conn.rollback()
