import sqlite3

from .store import Toko
from .User import User
databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)


class Manager(User) :

    __jumlahManager=0
    
    def __init__(self,username,password,cabang,status):
        Manager.__jumlahManager+=1
        super().__init__(username,password,cabang,status)
        self.__username=username
        self.__password=password
        self.idStatus=str(1).zfill(2)
        self.idJabatan= str(2).zfill(1)
        self.id =str(Manager.__jumlahManager).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        self.totalGaji=2500000
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
        
    def showInfo(self,username,status,jabatan):
        print("username : {} /n Status : {} /n Jabatan : {}".format(self.username,self.status,self.jabatan))

