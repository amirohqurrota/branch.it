import sqlite3

from .User import User,Owner,Manager,Karyawan
from .store import Toko as toko


databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

global namaObjek
   
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
        data=conn.cursor().execute("update barang set jumlahStok=? where idBarang=?",(self.jumlahStok,self.idBarang,))
        conn.commit()
        
    def setJumlahTerjual(self,jumlah):
        self.jumlahTerjual+=jumlah
        self.setJumlahStok(jumlah)
        self.totalKeuntungan()
        # print("-----",self.jumlahTerjual,"-------")
        data=conn.cursor().execute("update barang set jumlahTerjual=? where idBarang=?",(self.jumlahTerjual,self.idBarang,))
        conn.commit()
  

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
        # for row in listBarang:
        #     # namaObjek=exec(row+str(username.idCabang))
        #     # namaObjek.setJumlahTerjual(listBarang[row])
        #     getattr(str(row2)+str(username.idCabang),setJumlahTerjual(listBarang[row2]))
        #     #         # namaObjek=str(row2)+(username.idCabang)
        #     #         # namaObjek=eval(namaObjek)
        #     #         # # namaObjek.setJumlahTerjual(listBarang[row2])

        Order(username,cabang,self.totalTransaksi)
        cabang.setOmset(self.totalTransaksi)
        conn.execute("insert or ignore into transaksi values (?,?,?)" , (self.__idTransaksi,self.orderDate,self.totalTransaksi)) #masukkan ke database
        conn.commit()

  
    