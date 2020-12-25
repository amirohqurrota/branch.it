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

print(idUser)

b=str(3)

c=2
d=int(b)+c
print(d)
