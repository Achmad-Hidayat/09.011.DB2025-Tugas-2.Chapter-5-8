# Pohon_dict={"Mahoni":8,"Pinus":9,"Kelapa":10}
# print("Achamd Hidayat tanam :",Pohon_dic)

# dana_dict={"Swadaya":50,"Wajib": 20,"Koperasi":35 }
# print("Bendahara menyimpan dana:",dana_dic)

# pohon_dict={"Mangrove":15,"Kelapa":12,"Pinus":25}
# print(f"Achamd hidayat tanam pohon Mangrove: {pohon_dict['Mangrove']}")

# Dana_Desa={"Desa Bawah":100,"Desa Tengah":130,"Desa Atas":150}
# print(f"Bantuan UMKM telah disalurkan ke Ds.Cijeulang Sebesar(Rp):{Dana_Desa['Desa Tengah']}",end="")
# print("juta")

# Pohon_dict={"Mangrove":5,"Pinus":7,"Kelapa":8}
# Pohon_dict["Kelapa"]=15
# print(f"Achmad hidayat tanam pohon: ",Pohon_dict)

# Pohon_dict={"Mahoni":5,"Pinus":9}
# Pohon_dict["Gaharu"]=10
# print("Achamd hidayat tanam pohon:",Pohon_dict)

# Pohon_dict={"Mangrove":5,"Pinus":7,"Kelapa":8}
# Pohon_dict["Kelapa"]=10
# print("Achmad hidayat tanam pohon: ",Pohon_dict["Kelapa"])

# pohon_dict={}
# jumlah=int(input("Masukan jumlah pohon: "))
# for i in range (jumlah):
#     pohon = input(f"Masukan nama pohon ke-{i+1}: ")
#     jumlah_pohon=int(input(f"Masukan jumlah {pohon}: "))
#     pohon_dict[pohon]=jumlah_pohon
#     print("Achmad Hidayat tanam pohon:",pohon_dict)


# Pohon_dict={"Mahoni":8,"Gaharu":15,"Pinus":6}
# for pohon, jumlah in Pohon_dict.items():
#     print(f"Achmad Hidayat tanam {pohon}:{jumlah}!")

# pohon_dict = {"Mahoni": 8,"Mangrove": 10, "Pinus": 15}
# keys = list(pohon_dict.keys())
# i = 0
# while i <len (keys):
#     pohon = keys[i]
#     print(f"Achmad hidayat tanam {pohon}:{pohon_dict[pohon]}!")
#     i = i + 1

# pohon_dict={"Mahoni": 8, "Mangrove":10, "Gaharu":20}
# for pohon, jumlah in pohon_dict.items():
#     if jumlah>11:
#         print(f"Achmad Hidayat tanam {pohon}:{jumlah},banyak!")
#     else:
#         print(f"Achmad Hidayat tanam {pohon}:{jumlah},tambah lagi!")

# pohon_dict={}
# for i in range(3):
#     pohon=input(f"Masukan nama pohon ke-{i+1}: ")
#     jumlah=int(input(f"Masukan jumlah {pohon}: "))
#     pohon_dict[pohon]=jumlah    
# for pohon, jumlah in pohon_dict.items():
#     print(f"Achmad Hidayat tanam {pohon}:{jumlah}!")

# pohon_dict={"Mangrove": 10, "Gaharu": 12, "Mahoni":8, "Pinus":6}
# keys=list(pohon_dict.keys())
# i=0
# while i < len(keys):
#     pohon=keys[i]
#     jumlah=pohon_dict[pohon]
#     if jumlah >9:
#         print(f"Achmad Hidayat tanam {pohon}: {jumlah}, banyak!")
#     else:
#         print(f"Achmad hidayat tanam {pohon}:{jumlah}, tambah lagi")
#     i=i+1

# berat_dict={}
# jumlah=int(input("Masukan jumlah sampah: "))
# for i in range (jumlah):
#     jenis=input(f"Masukan jenis sampah ke-{i+1}: ")
#     berat=float(input(f"Masukan berat {jenis} (kg): "))
#     berat_dict[jenis]=berat
# total=0
# for berat in berat_dict.values():
#     total=total+berat
# print(f"Achmad Hidayat daur ulang {total} kg!")

# berat_dict={"Plastic":10.5,"Kardus":22.5,"Daun":11.5}
# for jenis, berat in berat_dict.items():
#     if berat > 11:
#         print(f"Achmad hidayat daur ulang {jenis}:{berat} kg, banyak!") 
#     else:
#         print(f"Achmad hidayat daur ulang {jenis}:{berat} kg, tambah lagi!")

# lampu_dict={}
# i=0
# while i < 3:
#     ruangan=input(f"Masukan ruangan ke-{i+1}: ")
#     lampu=int(input(f"masukan jumlah lampu di {ruangan}: "))
#     lampu_dict[ruangan]=lampu
#     i=i+1
# total=0
# for lampu in lampu_dict.values():
#     total=total+lampu
# print(f"Achmad hidayat hemat {total} lampu ")

# donasi_dict={"Panti Asuahan":2000000, "Masjid":1500000,"Madrasah":2500000}
# for tempat, donasi in donasi_dict.items():
#     if donasi>1700000:
#         print(f"Achmad hidayat donasi ke {tempat}: Rp{donasi}\nBanyak","buat komunitas!",sep=" =>",end=" ")
#         print("Indonesia hebat yuk!")
#     else:
#         print(f"Achmad hidayat donasi ke {tempat}:Rp{donasi}\nTambah lagi","buat komunitas",sep=" =>>",end=" ")
#         print("Indonesia hebat yuk!")

# berat_dict={}
# i=0
# while i < 3:
#     jenis=input(f"Masukan jenis sampah ke-{i+1}: ")
#     berat=float(input(f"Masukan berat {jenis} (kg): "))
#     berat_dict[jenis]=berat
#     i=i+1
# total=0
# for jenis, berat in berat_dict.items():
#     total=total+berat
#     if total>10:
#         print(f"Achmad Hodayat daur ulang {total} kg!\nCukup", f"{jenis} banyak!,",sep=" =>",end="")
#         print("Yuk !")
#     else:
#         print(f"Achmad Hidayat daur ulang {total} kg!\nTambah",f"{jenis} kurang!",sep=" =>",end="")
#         print("tambah yuk !")