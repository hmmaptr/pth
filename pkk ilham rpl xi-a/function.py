def Greeting(nama) :
    print("hallo", nama)

Greeting("Ilham")

#fungsi dengan mengembalikan nilai
def penjumlahan(a, b) :
    hasil = a + b 
    return hasil
 
hasil_penjumlahan = penjumlahan(7, 9)
print("hasil penjumlahan adalah", hasil_penjumlahan)
print(f"hasil penjumlahan adalah {hasil_penjumlahan}")

#fungsi dengan variable panjang argument(*args)
def jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    return total

hasil = jumlahkan(12, 30, 40, 50, 5, 3, 7, 0, 700, 1000)
print(f"hasil penjumlahan: {hasil}")