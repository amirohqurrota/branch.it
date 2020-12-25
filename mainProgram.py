import sqlite3

from User import User,Manager,Karyawan
 from Transaksi import Order,Transaksi,Barang




def showAll() :
    data=conn.cursor().execute("select*from user")  
    i=0
    for row in data:
        i+=1
        print("==Data-{}==".format(i))
        print("\t Id User: {} \n\t Username:{} \n\t Jabatan: {} \n\t Status: {}".format(row[0],row[1],row[3],row[2]))
        
def addUser():
    a=None
    idUser=int(input("masukkan id user :"))
    username=str(input("masukkan username user :"))
    password=str(input("masukkan password user :"))
    idStatus=int(input("masukkan id status :"))
    idJabatan=int(input("masukkan id jabatan :"))
    if idJabatan==0:
        jabatan=None
        a=User(idUser,username,password,idStatus,jabatan)
        listObject.append(a)
    elif idJabatan==1:
        Manager(idUser,username,password,idStatus)
        listObject.append(a)
    elif idJabatan==2:
        Karyawan(idUser,username,password,idStatus)
        listObject.append(a)
    else:
        print("id jabatan tidak ada")

def searchBy():
    choice=input("cari berdasarkan apa (tulis angka) \n\t 1. idUser \n\t 2.username \n\t 3.jabatan ")
    if choice=="1":
        search=input("masukkan id User ")
        data=conn.cursor().execute("select * from user where idUser=?",(search,))
        for row in data:
            print("\t Id User: {} \n\t Username:{} \n\t Jabatan: {} \n\t Status: {}".format(row[0],row[1],row[3],row[2]))
    elif choice=="2":
        search=input("masukkan username User :")
        data=conn.cursor().execute("select * from user where username=?",(search,))
        for row in data:
            print("\t Id User: {} \n\t Username:{} \n\t Jabatan: {} \n\t Status: {}".format(row[0],row[1],row[3],row[2]))
    elif choice=="3":
        jabatan=input("jabatan apa yang dicari (tulis angka) \n\t 1. karyawan \n\t 2.manager ")
        if jabatan=="1":
            data=conn.cursor().execute("select * from user where jabatan=?",("karyawan",))
            for row in data:
                print("==Data==")
                print("\t Id User: {} \n\t Username:{} \n\t Jabatan: {} \n\t Status: {}".format(row[0],row[1],row[3],row[2]))
        elif jabatan=="2":
            data=conn.cursor().execute("select * from user where jabatan=?",("Manager",))
            for row in data:
                print("==Data==")
                print("\t Id User: {} \n\t Username:{} \n\t Jabatan: {} \n\t Status: {}".format(row[0],row[1],row[3],row[2]))
        else:
            print("inputan salah")

#njalanin overloading yang sudah dibuat di super class user
def lihatGaji():
    print("PASTIKAN DATA YANG DIINPUTKAN BENAR YA,JIKA RAGU SILAHKAN LIHAT SEMUA DATA DULU")
    inputUsername=input("masukkan username yang ingin anda lihat total gajinya ")
    jabatan=input("ketikkan jabatan (karyawan/manager) ")
    gajiPokok=int(input("masukkan gaji pokok "))
    true=input("apakah ada uang lembur?(y/t)")
    if true=="y":
        uangLembur=int(input("masukkan total uang lembur "))
    else:
        uangLembur=None
    for ob in listObject:
        if ob.username==inputUsername:
            ob.totalGaji(jabatan,gajiPokok,uangLembur)
 
 #bikin objek dasar biar databasenya ada isinya


def menu():
    menuChoice=input("""
      ====SELAMAT DATANG====     
      Berikut pilihan menu (inputkan angka pilihan):
        1. Melihat semua data user
        2. Mencari data user
        3. Menambahkan user baru
        4. Tampilkan total gaji user
      """)
    if menuChoice=="1":
        showAll()
    elif menuChoice=="2":
        searchBy()
    elif menuChoice=="3":
        addUser()
    elif menuChoice=="4":
        lihatGaji() 
    else:
        print("masukkan ulang pilihan menu")     
        menu()

#buat object biar database ada isinya
listObject=[]

a=Manager(10,"anisaa","1234567",1)
listObject.append(a)
kaeha=Manager(4,"kaeha","1234567",1)
listObject.append(kaeha)
nobita=Karyawan(5,"nobita","1234567",0)
listObject.append(nobita)
suneo=Karyawan(6,"suneo","1234567",1)
listObject.append(suneo)
siapaa=Karyawan(7,"siapaa","1234567",1)
listObject.append(siapaa)

menu()