nilai = int(input("masukan nilai anda: "))
eskul = input("apakah anda ikut eskul (ya/tidak): ")

if nilai > 89:
    if eskul == "ya":
        nilai_akhir = "A+"
    else:
        nilai_akhir = "A"
print ("nilai akhir anda:", nilai_akhir)


