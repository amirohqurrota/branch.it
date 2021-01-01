
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

#login()
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

#absenKehadiran()
def absenKehadiran(username):
    username.setJumlahAbsensi()
    print("Absensi telah ditambahkan, Selamat Bekerja!")


def cekStokToko(username,cabang):
    id=Toko.getIdCabang(cabang)
    data=conn.cursor().execute("select * from barang where idCabang=?",(id,))
    for row in data:
        print("{}\t stok : {}".format(row[1],row[4]))

# cekStokSemuaToko()
def cekStokSemuaToko():
    listId=list(Toko.getCabangDict().values())
    for i in listId:
        print("=====STOK TOKO {}=====".format(Toko.getCabangbyId(i)).upper())
        data=conn.cursor().execute("select * from barang where idCabang=?",(i,))
        for row in data:
            print("{}\t stok : {}".format(row[1],row[4]))

# cekStokSemuaToko()
#membuat transaksi
def cetakTransaksi(username,cabang):
    cekStokToko(username,cabang)
    tgl=input("masukkan tanggal :")
    daftar=input("tuliskan list barang beserta stoknya dalam bentuk dictionary")
    Transaksi(tgl,daftar,username,cabang)
    
#cetakTransaksi(karyawan1,"madiun")
Transaksi("22/2/20",{apel:2,jeruk:1},karyawan1,madiun)

def tampilkanOmsetSemuaToko():
    # idCabang=input("masukkan cabang yang ingin ditampilkan :")
    # cabang.tampilkanInfo()
    listId=list(Toko.getCabangDict().values())
    for i in listId:
        data=conn.cursor().execute("select * from toko where idCabang=?",(i,))
        for row in data:
            print("Toko {}\t Omset : {}".format(row[1],row[2]))


#=============
def daftarAbsensiKaryawan(cabang):
    idCabang=Toko.getIdCabang(cabang)
    data=conn.cursor().execute("select idUser,username,jumlahAbsensi from user")
    for row in data:
        if row[0][0]==str(3) and row[0][5]==str(idCabang):
            print("Nama : {} \t jumlahAbsensi : {} ".format(row[1],row[2]))
            break

# daftarAbsensiKaryawan("madiun")

#print(Toko.getIdCabang(a))
# print(Toko.getCabangbyId(3))
#print(Toko.getCabangDict())

def menu():
    while True:
        print("Halooo selamat datang di program kami, untuk melanjutkan silahkan login terlebih dahulu")
        username=input("masukkan username ")
        password=input("masukkan password ")
        a=conn.cursor().execute("select * from user where username=? AND password=?",(username,password))
        result=a.fetchall()
        #print(result)
        if result:
            print("selamat datang di Branch.it {}".format(username))
        else:
            print("maaf, username dan password yang anda masukkan salah. silahkan coba kembali")
            break
        idUser=None
        idCabang=None
        x=conn.cursor().execute("select idUser from user where username=?",(username,)).fetchall()
        for row in x:
            idUser=row[0]
            idCabang=row[0][5]
            idJabatan=row[0][0]
        cabang=Toko.getCabangbyId(int(idCabang))

        if idJabatan=="1":
            print("""
            Selamat datang Owner, berikut pilihan menu yang tersedia :
                1. 
            """)
            break
        elif idJabatan=="2":
            print("""
            Selamat datang Bapak/Ibu Manager, berikut pilihan menu yang tersedia :
                1. 
            """)
            break
        elif idJabatan=="3":
            print("""
            Selamat datang {}, berikut pilihan menu yang tersedia :
                1. 
            """.format(username))
            break

        #print(username,idJabatan,idCabang,cabang)

menu()


    










