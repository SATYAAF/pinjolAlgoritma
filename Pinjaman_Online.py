nama = str(input("Masukan nama : "))
umur = int(input("Masukan umur : "))
alamat= str(input("Masukan alamat : "))
nomer_rekening = (input("Masukan nomer rekening anda :"))
jumlah_nominal_pinjaman = float(input("Masukan nominal pinjaman :"))
jumlah_cicilan_perbulan = float(input("Masukan cicilan :"))
pekerjaan = str(input("Masukan pekerjaan :"))
penghasilan_perbulan= float(input("Masukan penghasilan perbulan :"))

print([nama,umur,alamat,])
print([pekerjaan])

if umur <= 20 and penghasilan_perbulan <= 1000000: 
    print("MAAF ANDA TIDAK MEMENUHI SYARAT PEMINJAMAN")
else: 
    print("SELAMAT ANDA DAPAT MEMINJAM UANG DI BANK SWASTA SATYAADIL SILAKAN TUNGGU SAMPAI KAMI CAIRKAN")   