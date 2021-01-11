import sqlite3
from method import *

databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)

conn.execute("DROP TABLE IF EXISTS orderTabel")
conn.execute("CREATE TABLE IF NOT EXISTS orderTabel(idOrder primary key,idUser str ,totalBelanja int)")

conn.execute("DROP TABLE IF EXISTS transaksi")
conn.execute("CREATE TABLE IF NOT EXISTS transaksi  (idTransaksi int primary key,orderDate str ,totalTransaksi int)")

conn.execute("DROP TABLE IF EXISTS barang")
conn.execute("CREATE TABLE IF NOT EXISTS barang  (idBarang int primary key,namaBarang str ,idCabang str,harga int,jumlahStok int,jumlahTerjual int, keuntungan int)")

conn.execute("DROP TABLE IF EXISTS user")
conn.execute("CREATE TABLE IF NOT EXISTS user  (idUser int primary key,username text ,password text, jumlahAbsensi int ,  totalGaji int)")

conn.execute("DROP TABLE IF EXISTS toko")
conn.execute("CREATE TABLE IF NOT EXISTS toko (idCabang int primary key,namaCabang text ,omset int)")


#mbuat database
amiroh=Owner("amiroh","12345678",None,None)
sidoarjo=Toko("sidoarjo")
madiun=Toko("madiun")
surabaya=Toko("surabaya")
kediri=Toko("kediri")

# print(Toko.getCabangDict())

budi=Manager("budi","9876543","madiun",None)
arif=Manager("arif","3456789","sidoarjo",None)
sisi=Manager("sisi","098765","surabaya",None)
ike=Manager("ike","12345","kediri",None)

#karyawannya madiun
madiun1=Karyawan("madiun1","qwertyu","madiun","Karyawan Tetap")
madiun2=Karyawan("madiun2","qwertyuu","madiun","Karyawan Tetap")
madiun3=Karyawan("madiun3","qwertyuu","madiun","Karyawan Magang")
#karyawannya surabaya
surabaya1=Karyawan("surabaya1","qwertyu","surabaya","Karyawan Tetap")
surabaya2=Karyawan("surabaya2","qwertyuu","surabaya","Karyawan Tetap")
surabaya3=Karyawan("surabaya3","qwertyuu","surabaya","Karyawan Magang")
#karyawannya sidoarjo
sidoarjo1=Karyawan("sidoarjo1","qwertyu","sidoarjo","Karyawan Tetap")
sidoarjo2=Karyawan("sidoarjo2","qwertyuu","sidoarjo","Karyawan Tetap")
sidoarho3=Karyawan("sidoarho3","qwertyuu","sidoarjo","Karyawan Magang")
#karyawannya kediri
kediri1=Karyawan("kediri1","qwertyu","kediri","Karyawan Tetap")
kediri2=Karyawan("kediri2","qwertyuu","kediri","Karyawan Tetap")
kediri3=Karyawan("kediri3","qwertyuu","kediri","Karyawan Magang")


#STOK BARANG

asus1=Barang("asus",2000000,0.4,20,1)
acer1=Barang("acer",3000000,0.3,10,1)
mac1=Barang("mac",10000000,0.4,10,1)

asus2=Barang("asus",2000000,0.4,20,2)
acer2=Barang("acer",3000000,0.3,10,2)
mac2=Barang("mac",10000000,0.4,10,2)

asus3=Barang("asus",2000000,0.4,20,3)
acer3=Barang("acer",3000000,0.3,10,3)
mac3=Barang("mac",10000000,0.4,10,3)

asus4=Barang("asus",2000000,0.4,10,4)
acer4=Barang("acer",3000000,0.3,10,4)
mac4=Barang("mac",10000000,0.4,10,4)

#TRANSAKSI
a="madiun1"
b=eval(a)
#Order(b,madiun,2000000)
Transaksi("2012-12-2",{"asus":1},sidoarjo2,sidoarjo)
asus1.setJumlahTerjual(1)

Transaksi("2012-12-2",{"mac":2},sidoarjo1,sidoarjo)
mac1.setJumlahTerjual(2)

Transaksi("2012-12-2",{"acer":3},sidoarjo2,sidoarjo)
acer1.setJumlahTerjual(3)

#madiun
Transaksi("2012-12-2",{"asus":1},madiun2,madiun)
asus2.setJumlahTerjual(1)

Transaksi("2012-12-2",{"mac":3},madiun1,madiun)
mac2.setJumlahTerjual(3)

Transaksi("2012-12-2",{"acer":1},madiun3,madiun)
acer2.setJumlahTerjual(1)
# # Transaksi("2012-12-2",{"mac":1},madiun2,madiun)
# # Transaksi("2012-12-2",{"mac":1},madiun2,madiun)
# a="asus"
# b="2"
# c=a+b
# c=eval(c)
# print(c.namaBarang)
