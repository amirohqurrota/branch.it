import sqlite3

from .store import Toko
from .User import User
databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)

class Karyawan(User) :
    __jumlahKaryawan=0
    __statusDict = {"Karyawan Tetap": 1,"Karyawan Tidak Tetap": 2,"Karyawan Magang":3}
    @classmethod  #agar method nempel di class bukan di object 
    def listStatus(cls,status): #override method listStatus yang ada di user
        idStatus=str((Karyawan.__statusDict[status])).zfill(2)
        return idStatus

    @classmethod  #agar method nempel di class bukan di object 
    def listGajiPokok(cls,idStatus): #override method listStatus yang ada di user
        gajiPokokDict={1:1500000,2:1000000,3:500000}
        gajiPokok=gajiPokokDict[int(idStatus)]
        return gajiPokok
        
    @classmethod
    def getStatusDict(cls):
        return Karyawan.__statusDict
    
    def __init__(self,username,password,cabang,status):
        Karyawan.__jumlahKaryawan+=1
        super().__init__(username,password,cabang,status)
        self.__username=username
        self.__password=password
        self.idJabatan= str(3).zfill(1)
        self.id =str(Karyawan.__jumlahKaryawan).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        self.totalGaji=self.listGajiPokok(self.idStatus)
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
    def showInfo(self):
        print("username : {} /n Jabatan : {} /n Status : {}".format(self.username,self.jabatan,self.status))
