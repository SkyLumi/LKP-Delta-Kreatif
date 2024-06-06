import psycopg2
def database():
    connect = psycopg2.connect(database='LKP Delta Kreatif', user='postgres', password='bebas', host='localhost', port=5432)
    return connect