import sqlite3

from .User import User
from .Owner import Owner
from .Manager import Manager
from .Karyawan import Karyawan
from .store import Toko as toko
from .Order import Order


databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)

class Barang:
    __jumlahBarang=0
    def __init__(self,namaBarang,harga,keuntungan,jumlahStok,idcabang):
        Barang.__jumlahBarang+=1
        self.idCabang=str(idcabang)
        self.id =str(Barang.__jumlahBarang).zfill(4)
        self.idBarang=self.idCabang+"-"+self.id
        self.namaBarang=namaBarang
        self.__harga=harga
        self.keuntungan=self.__harga*keuntungan
        self.jumlahStok=jumlahStok
        self.jumlahTerjual=0
        conn.execute("insert or ignore into barang values (?,?,?,?,?,?,?)" , (self.idBarang,self.namaBarang,self.idCabang,self.__harga,self.jumlahStok,self.jumlahTerjual,self.keuntungan)) #masukkan ke database
        conn.commit()
        
   
    def getHarga(self):
        return self.__harga
    
    def totalKeuntungan(self):
        total=self.jumlahTerjual*self.keuntungan
        return total
    
    def setJumlahStok(self,jumlah):
        self.jumlahStok-=jumlah
        conn.cursor().execute("update barang set jumlahStok=? where idBarang=?",(self.jumlahStok,self.idBarang,))
        conn.commit()

       
    def setJumlahTerjual(self,jumlah):
        self.jumlahTerjual+=jumlah
        self.setJumlahStok(jumlah)
        self.totalKeuntungan()
        # print("-----",self.jumlahTerjual,"-------")
        conn.cursor().execute("update barang set jumlahTerjual=? where idBarang=?",(self.jumlahTerjual,self.idBarang,))
        conn.commit()
 