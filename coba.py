#print (f"{10:04d}")
a=str(29).zfill(3)
print(a)

jabatanDict = {"Owner": 1,"Manager": "2","Karyawan":3}
jabatan=str((jabatanDict["Karyawan"])).zfill(1)
statusDict = {"Karyawan Tetap": 1,"Karyawan Tidak Tetap": 2,"Karyawan Magang":3}
status=str((statusDict["Karyawan Tetap"])).zfill(2)
cabangDict={"Jember":1,"Pondok Gede":2, "Caipan":3,
            "POndok Jati":4,"Pondok Mutiara":5,"Green Hill":6,
            "Wilang Bango":7,"Madalengka":8,"Bursa":9}
cabang=str((cabangDict["Pondok Mutiara"])).zfill(2)
jumlahKaryawan=str(9).zfill(3)
idUser=jabatan+"-"+status+"-"+cabang+"-"+jumlahKaryawan

# print(idUser)

# b=str(3)

# c=2
# d=int(b)+c
# print(d)

# a={"laptop":3,"motor":2}
# print(a["laptop"])
# for i in a:
#     print(a[i])

# a=str(123)
# b=str(a[0])+str(a[1])
# print(b)
# a={"sidoarjo":1,"madiun":2}
# #print(a["sidoarjo"]) 
# for b in a:
#     print(a[b])
a={'apel': 1, 'jeruk': 2, 'mangga': 3}
# for i in listt:
#      print (listt[i])

key_list = list(a.keys())
val_list = list(a.values())
print(val_list)
# a=1
# position=val_list.index(a)
# print(key_list[position])


# import sqlite3

# databaseName='iniDBbuatCoba.db'
# conn = sqlite3.connect(databaseName)
# namaBarang='apel'
# idCabang='1'
# data=conn.cursor().execute("select idBarang from barang where namaBarang=? and idCabang=?",(namaBarang,idCabang,))
# print (data[0])

# my_data = '1-23-06'
# parsed = my_data.split('-')
# print(parsed)