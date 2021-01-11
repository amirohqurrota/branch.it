import sqlite3

from .User import User
from .Owner import Owner
from .Manager import Manager
from .Karyawan import Karyawan
from .store import Toko as toko
from .Order import Order
from .Barang import Barang


databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)

class Transaksi:
    __jumlahTransaksi=0
    def __init__(self,orderDate,listBarang,username,cabang):
        Transaksi.__jumlahTransaksi+=1
        self.idUserTransaksi=username.idUser
        self.id =str(Transaksi.__jumlahTransaksi).zfill(4)
        self.__idTransaksi=str(username.idCabang)+"-"+str(username.id)+"-"+str(self.id)
        self.orderDate=orderDate
        self.listBarang=listBarang
        self.totalTransaksi=0
        data=conn.cursor().execute("select * from barang where idCabang=?",(username.idCabang,))
        for row1 in data:
            for row2 in self.listBarang:
                if row1[1]==row2:
                    total=row1[3]*self.listBarang[row2]
                    self.totalTransaksi+=total


        Order(username,cabang,self.totalTransaksi)
        cabang.setOmset(self.totalTransaksi)
        conn.execute("insert or ignore into transaksi values (?,?,?)" , (self.__idTransaksi,self.orderDate,self.totalTransaksi)) #masukkan ke database
        conn.commit()
