import sqlite3

databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

from method import *

#mbuat database
amiroh=Owner("amiroh","12345678",None,None)
sidoarjo=Toko("sidoarjo")
madiun=Toko("madiun")
surabaya=Toko("surabaya")

budi=Manager("budi","9876543","madiun",None)
arif=Manager("arif","3456789","sidoarjo",None)
sisi=Manager("sisi","098765","surabaya",None)

karyawan1=Karyawan("karyawan1","qwertyu","madiun","Karyawan Tetap")
karyawan2=Karyawan("karyawan2","qwertyuu","madiun","Karyawan Tetap")

karyawan3=Karyawan("karyawan3","qqwertyu","sidoarjo","Karyawan Magang")
karyawan4=Karyawan("karyawan4","qwerttyu","surabaya","Karyawan Tetap")

apel=Barang("apel",20000,0.4,20,2)
apel=Barang("apel",20000,0.4,10,1)
apel=Barang("apel",20000,0.4,15,3)

jeruk=Barang("jeruk",20000,0.4,20,2)
jeruk=Barang("jeruk",20000,0.4,10,1)
jeruk=Barang("jeruk",20000,0.4,15,3)

def login():
    username=input("masukkan username ")
    password=input("masukkan password ")
    a=conn.cursor().execute("select * from user where username=? AND password=?",(username,password))
    result=a.fetchall()
    print(result)
    if result:
        print("selamat datang di Branch.it {}".format(username))
    else:
        print("maaf, username dan password yang anda masukkan salah. silahkan coba kembali")

#login()

def absenKehadiran(username):
    username.setJumlahAbsensi()
    print("Absensi telah ditambahkan, Selamat Bekerja!")
    
#absenKehadiran(arif)
def cekStokToko(username,cabang):
    id=Toko.getIdCabang(cabang)
    data=conn.cursor().execute("select * from barang where idCabang=?",(id,))
    for row in data:
        print("{}\t stok : {}".format(row[1],row[4]))

def cetakTransaksi(username,cabang):
    cekStokToko(username,cabang)
    tgl=input("masukkan tanggal :")
    list=input("tuliskan list barang beserta stoknya dalam bentuk dictionary")
    Transaksi(tgl,list,username)
    
# cetakTransaksi(karyawan3,surabaya)

    
cetakTransaksi(karyawan3,"sidoarjo")

def





