from koneksi import connection

def takeData(key) : 
    koneksi = connection()

        # Membuat objek cursor
    cursor = koneksi.cursor()

        # Contoh query
    query = f"SELECT * FROM answer WHERE question LIKE '%{key}%';"

        # Mengeksekusi query
    cursor.execute(query)

        # Mendapatkan hasil query
    hasil = cursor.fetchall()

        # Menampilkan hasil
    dataFinal = []
    for baris in hasil:
        dataFinal = (list(baris))
        return dataFinal
        # Menutup kursor
        