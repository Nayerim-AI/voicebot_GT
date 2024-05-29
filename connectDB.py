import mysql.connector

def connection():
    host = 'localhost'
    database = 'voice'
    user = 'root'
    password = ''  # Ganti dengan password MySQL Anda

    try:
        koneksi = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        return koneksi
    except mysql.connector.Error as err:
        print(f"Error: {err}")
