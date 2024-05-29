from connectDB import connection

def takeData(key):
    koneksi = connection()
    if koneksi:
        cursor = koneksi.cursor()
        query = f"SELECT * FROM answer WHERE question LIKE '%{key}%';"
        cursor.execute(query)
        hasil = cursor.fetchall()
        dataFinal = []
        for baris in hasil:
            dataFinal = (list(baris))
            return dataFinal
    else:
        print("Koneksi ke database gagal.")
