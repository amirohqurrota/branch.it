import sqlite3
from User import User,Manager,Karyawan

databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

conn.execute("DROP TABLE IF EXISTS orderTabel")
conn.execute("CREATE TABLE IF NOT EXISTS orderTabel(idOrder primary key,idUser str ,totalBelanja int)")

conn.execute("DROP TABLE IF EXISTS transaksi")
conn.execute("CREATE TABLE IF NOT EXISTS transaksi  (idTransaksi int primary key,orderDate str ,totalTransaksi int)")

conn.execute("DROP TABLE IF EXISTS barang")
conn.execute("CREATE TABLE IF NOT EXISTS barang  (idBarang int primary key,namaBarang str ,harga int,jumlahStok int,jumlahTerjual int, keuntungan int)")

   
class Order:
    __jumlahOrder=0
    def __init__(self,username,totalBelanja):
        Order.__jumlahOrder+=1
        self.id =str(Order.__jumlahOrder).zfill(4)
        self.idOrder=username.idCabang+"-"+username.id+"-"+self.id
        self.totalBelanja=totalBelanja
        totalFee=0.15*totalBelanja
        username.setTotalFee(totalFee)
        self.idUserOrder=username.idUser
        conn.execute("insert or ignore into orderTabel values (?,?,?)" , (self.idOrder,self.idUserOrder,self.totalBelanja)) #masukkan ke database
        conn.commit()
        
               
class Transaksi:
    __jumlahTransaksi=0
    def __init__(self,orderDate,listBarang,username):
        Transaksi.__jumlahTransaksi+=1
        self.idUserTransaksi=username.idUser
        self.id =str(Transaksi.__jumlahTransaksi).zfill(4)
        self.idTransaksi=username.idCabang+"-"+username.id+"-"+self.id
        self.orderDate=orderDate
        self.listBarang=listBarang
        self.totalTransaksi=0
        for i in listBarang:
           total=listBarang[i]*i.harga
           self.totalTransaksi+=total
           i.setJumlahTerjual(listBarang[i])
        Order(username,self.totalTransaksi)
        conn.execute("insert or ignore into transaksi values (?,?,?)" , (self.idTransaksi,self.orderDate,self.totalTransaksi)) #masukkan ke database
        conn.commit()
        
    
class Barang:
    __jumlahBarang=0
    def __init__(self,namaBarang,harga,keuntungan,jumlahStok,idcabang):
        Barang.__jumlahBarang+=1
        self.idCabang=idcabang
        self.id =str(Barang.__jumlahBarang).zfill(4)
        self.idBarang=self.idCabang+"-"+self.id
        self.namaBarang=namaBarang
        self.harga=harga
        self.keuntungan=self.harga*keuntungan
        self.jumlahStok=jumlahStok
        self.jumlahTerjual=0
        conn.execute("insert or ignore into barang values (?,?,?,?,?,?)" , (self.idBarang,self.namaBarang,self.harga,self.jumlahStok,self.jumlahTerjual,self.keuntungan)) #masukkan ke database
        conn.commit()
        
    def totalKeuntungan(self):
        total=self.jumlahTerjual*self.keuntungan
        return total
    
    def setJumlahStok(self,jumlah):
        self.jumlahStok-=jumlah
        
    def setJumlahTerjual(self,jumlah):
        self.jumlahTerjual+=jumlah
        self.setJumlahStok(jumlah)
        self.totalKeuntungan()
        
amiroh=Karyawan("amiroh","12345678","Green Hill","Karyawan Tetap",)
Apel=Barang("apel",5000,0.5,40,"Green Hill")
Jeruk=Barang("jeruk",7000,0.4,20,"Green Hill")
Sawo=Barang("sawo",10000,0.6,10,"Green Hill")
a=Transaksi("09-10-20",{Apel:2,Jeruk:10},amiroh)
print(Apel.jumlahStok)
print(Apel.jumlahTerjual)
print(Apel.keuntungan)
print(amiroh.totalGaji)


# woy=Karyawan("woy","12345678","Jember","Karyawan Tetap",)
# woyy=Manager("woyy","12345678","Green Hill","Karyawan Magang",)
# woyy.setTotalFee(2000000)
# woyy.setJumlahAbsensi()      
# woyy.setJumlahAbsensi()
    
# order1=Order(woy,500000)

# print(woy.totalGaji)
# # print(tono.__dict__)
    
    