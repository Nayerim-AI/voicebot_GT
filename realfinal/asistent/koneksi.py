import mysql.connector

# Mengganti nilai-nilai berikut sesuai dengan konfigurasi database Anda
host = 'localhost'
database = 'voice'
user = 'root'
password = ''

def connection() :
    try:
        # Membuat koneksi
        koneksi = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        # Memeriksa apakah koneksi berhasil
        # if koneksi.is_connected():
            # print(f"Berhasil terhubung ke database '{database}'")
            
        # Melakukan operasi database di sini
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Menutup koneksi, bahkan jika terjadi exception
        if 'koneksi' in locals() and koneksi.is_connected():
            return koneksi
