import sqlite3

from .User import User
from .Owner import Owner
from .Manager import Manager
from .Karyawan import Karyawan
from .store import Toko as toko


databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)


   
class Order:
    __jumlahOrder=0
    def __init__(self,username,cabang,totalBelanja):
        #usernameObjek=eval(username)
        Order.__jumlahOrder+=1
        self.id =str(Order.__jumlahOrder).zfill(4)
        self.__idOrder=str(username.idCabang)+"-"+str(username.id)+"-"+self.id
        self.totalBelanja=totalBelanja
        totalFee=0.15*totalBelanja
        username.setTotalFee(totalFee)
        self.idUserOrder=username.idUser
        conn.execute("insert or ignore into orderTabel values (?,?,?)" , (self.__idOrder,self.idUserOrder,self.totalBelanja)) #masukkan ke database
        conn.commit()
    
   
    def getIdOrder(self):
        return self.__idOrder

    
 

