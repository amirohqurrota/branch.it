
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


def cekStokToko(cabang):
    id=Toko.getIdCabang(str(cabang))
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
    cekStokToko(cabang)
    tgl=input("masukkan tanggal :")
    listTransaksi=input("tuliskan list barang beserta stoknya dalam bentuk dictionary")
    listTransaksi=eval(listTransaksi)
    cabangObjek=eval(cabang)
    Transaksi(tgl,listTransaksi,username,cabangObjek)
# Transaksi("22/2/20",{apel:2,jeruk:1},karyawan1,madiun)

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

def tambahBarang():
    namaBarang=input("masukkan nama barang")
    harga=int(input("masukkan harga barang"))
    keuntungan=float(input("masukkan persentase keuntungan"))
    jumlahStok=int(input("masukkan jumlah stok yang tersedia"))
    namaBarang=Barang(namaBarang,harga,keuntungan,jumlahStok,idCabang)

def ubahStok(idCabang):
    cekStokToko(str(cabang))
    namaBarang=input("masukkan nama barang yang ingin diubah")
    idBarang=None
    data=conn.cursor().execute("select idBarang from barang where namaBarang=? and idCabang=?",(namaBarang,idCabang,))
    for row in data:
        idBarang=row[0]
    jumlah=int("masukkan update jumlah barang")
    data=conn.cursor().execute("update barang set jumlahStock=? where idBarang=?",(jumlah,idBarang,))
    conn.commit()

def tampilkanListHargaBarang(idCabang):
    
    data=conn.cursor().execute("select * from barang where idCabang=?",(idCabang,))
    for row in data:
        print ("Nama Barang : {} \t harga : {}".format(row[1],row[3]))


def menuOwner():
    print("""
            Selamat datang Owner, berikut pilihan menu yang tersedia :
                1. Melihat identitas tiap toko
                2. Melihat rekapitulasi penjualan di semua toko
                3. Melihat data stok barang di semua toko 

            """)
    pilihan=input("masukkan angka pilihan menu : ")

def menuManager():
    print("""
            Selamat datang Bapak/Ibu Manager, berikut pilihan menu yang tersedia :
            1. Menambahkan data identitas tiap toko
            2. Melihat data identitas tiap toko
            3. Menambahkan data barang
            3. Menambahkan data karyawan 
            4. Melihat data kehadiran karyawan
            5. Melihat rekapitulasi penjualan per toko
            6. Melihat data stok barang per toko

            """)
    pilihan=input("masukkan angka pilihan menu : ")

def menuKaryawan():
    absenKehadiran(objek)
    print("""
            Selamat datang {}, berikut pilihan menu yang tersedia :
            1. Mengubah stok barang
            2. Melihat list data harga barang
            3. Membuat data transaksi penjualan
            4. Melihat data stok barang
            5. Exit
            """.format(username))
    pilihan=input("masukkan angka pilihan menu : ")
    if pilihan==1:
        ubahStok(idCabang)
    elif pilihan==2:
        tampilkanListHargaBarang(idCabang)
    elif pilihan==3:
        cetakTransaksi(usernameObjek,cabang)
    elif pilihan==4:
        cekStokToko(cabang)
    elif pilihan==5:
        print("terimakasih, sampai ketemu besok!")





def menuLanding():
    while True:
        global idUser
        global idCabang
        global idJabatan
        global username
        global usernameObjek
        global objek
        global cabang
        print("Halooo selamat datang di program kami, untuk melanjutkan silahkan login terlebih dahulu")
        username=input("masukkan username ")
        usernameObjek=eval(username)
        password=input("masukkan password ")
        a=conn.cursor().execute("select * from user where username=? AND password=?",(username,password))
        result=a.fetchall()
        #print(result)
        if result:
            print("selamat datang di Branch.it {}".format(username))
        else:
            print("maaf, username dan password yang anda masukkan salah. silahkan coba kembali")
            break
        
        x=conn.cursor().execute("select idUser from user where username=?",(username,)).fetchall()
        for row in x:
            idUser=row[0]
            idCabang=row[0][5]
            idJabatan=row[0][0]
        cabang=Toko.getCabangbyId(int(idCabang))
        objek=eval(username)
        if idJabatan=="1":
            menuOwner()
            break
        elif idJabatan=="2":
            menuManager
            break
        elif idJabatan=="3":
            menuKaryawan()
            break

        #print(username,idJabatan,idCabang,cabang)




    










