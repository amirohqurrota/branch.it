import sqlite3

from .store import Toko
from .User import User
databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)


class Owner(User):
    __jumlahOwner=1
    
    @classmethod  #agar method nempel di class bukan di object 
    def listStatus(cls,idStatus): #override method listStatus yang ada di user
        None
    
    def __init__(self,username,password,cabang,status):
        super().__init__(username,password,cabang,"Owner")
        self.__password=password
        self.idJabatan=str(1).zfill(1)
        self.idStatus=str(0).zfill(2)
        self.idCabang=str(0).zfill(2)
        self.id =str(Owner.__jumlahOwner).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
    def showInfo(self):
        print("username : {} /n Jabatan : {} /n Status : {}".format(self.username,self.jabatan,self.status))
