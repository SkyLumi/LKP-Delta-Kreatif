import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)

cur = conn.cursor()

def readPelatih():
    query = "SELECT * FROM pelatih"
    cur.execute(query)
    data = cur.fetchall()
    
    if data:

        colnames = [desc[0] for desc in cur.description]

        print(tabulate(data, headers=colnames, tablefmt='grid'))
    else:
        print("Tidak ada data pada tabel pelatih.")

def homepagePelatih():
    print('ini homepage pelatih')
