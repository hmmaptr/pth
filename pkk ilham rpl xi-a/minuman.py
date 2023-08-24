minuman = ["air zamzam", "freshtea", "coca-cola", "pepsi", "teh kotak"]
print(minuman[2])

#append itu menambah data dari belakang 
minuman.append("Marimas")

#prepend itu menambahkan dari depan 
minuman.pop(2)
print(minuman)

makanan = ("nasi tutug oncom", "sate", "baso", "seblak", "indomie" )
update = list(makanan)
update[0] = "nasi timbel"
tuple = tuple(update)
print(tuple)