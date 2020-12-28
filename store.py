import sqlite3
from User import User,Manager,Karyawan
from Transaksi import Transaksi,Order,Barang

databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

conn.execute("DROP TABLE IF EXISTS toko)
conn.execute("CREATE TABLE IF NOT EXISTS toko(idOrder primary key,idUser str ,totalBelanja int)")

class Toko ():
    @classmethod  #agar method nempel di class bukan di object 
    def listCabang(cls,cabang): #override method listStatus yang ada di user
        cabangDict={"Jember":1,"Pondok Gede":2, "Caipan":3,
            "Pondok Jati":4,"Pondok Mutiara":5}
        idCabang=str((cabangDict[cabang])).zfill(2)
        return idCabang
    
    def __init__(self,cabang):
        self.namaCabang=cabang
        self.listBarang={}
        self.omset=0
        self.idCabang=self.listCabang(cabang)
        conn.execute("insert or ignore into toko values (?,?,?,?,?)" , (self.idCabang,self.namaCabang,self.omset,self.listBarang) #masukkan ke database
        conn.commit()

    def setOmset():
         