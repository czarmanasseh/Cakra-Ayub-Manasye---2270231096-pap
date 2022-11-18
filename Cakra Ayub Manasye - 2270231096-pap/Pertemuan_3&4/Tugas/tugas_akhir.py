print("""
===================================
 Toko Komputer Banteng Merah
 Daftar Laptop yang Tersedia
 Jl. Raya Hankam
 Pondok Gede-Kota Bekasi
===================================
A. MSI : Rp 10.000.000
B. HP : Rp 5.000.000
C. RAZER : Rp 20.000.000
D. MACBOOK : Rp 15.000.000
===================================""")
nama=input("Nama Pembeli : ")
pesan=str(input("Nama Produk : "))
jumlahpesanan=int(input("Jumlah Unit : "))
if pesan == "MSI":
 harga=(10000000*jumlahpesanan)
elif pesan == "HP":
 harga=(5000000*jumlahpesanan)
elif pesan == "RAZER":
 harga=(20000000*jumlahpesanan)
elif pesan == "MACBOOK":
 harga=(15000000*jumlahpesanan)
else:
 pesan="-"
 harga= "-"
 pilihan=input("Menu Tidal Tersedia, silakan ulangi kembali Y/N ")
ppn = 20000+harga
print("-----------------------------------")
print("Harga Satuan : Rp.{}".format(harga))
print("PPN : Rp.20000")
print("Total : Rp.{}".format(ppn))
print("-----------------------------------")
print(" Semua Produk Memiliki Garansi")
print(""" Silahkan hubungi kami dibawah ini
 Telp.0812-5008-3237 
 Email : banteng.17ags@pdip.com
============TERIMA KASIH===========
""")