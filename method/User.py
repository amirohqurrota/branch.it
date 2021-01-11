import sqlite3

from .store import Toko
databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)


class User :
    jumlah=0
        
    @staticmethod  #agar method nempel di class bukan di object 
    def listStatus(status): #override method listStatus yang ada di user
        None


    def __init__(self,username,password,cabang,status):
        User.jumlah+=1
        self.username=username
        self.password=password
        self.idJabatan= str(0)
        if status==None:
            self.idStatus=00
        else:
            self.idStatus= self.listStatus(status) #status nya akan memanggil method listStatus 
        if cabang==None:
            self.idCabang=str(00)
        else:
            self.idCabang= Toko.getIdCabang(cabang)
        self.id =str(User.jumlah).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        self.totalFee=0
        self.jumlahAbsensi=0
        self.totalGaji=0
        
        
    def setTotalFee(self,fee):
        self.totalFee+=fee
        self.setTotalGaji(fee)
 
    def setTotalGaji(self,fee):
        self.totalGaji+=fee
        data=conn.cursor().execute("update user set totalGaji=? where idUser=?",(self.totalGaji,self.idUser,))
        conn.commit()
        
    def setJumlahAbsensi(self):
        self.jumlahAbsensi+=1
        self.setTotalFee(20000)
        data=conn.cursor().execute("update user set jumlahAbsensi=? where idUser=?",(self.jumlahAbsensi,self.idUser,))
        conn.commit()
     
    # def totalGaji(self,jabatan,gajiPokok,uangLembur=None): #overloading
    #     if jabatan=="karyawan":
    #         feeJabatan=1500000
    #     elif jabatan=="manager":
    #         feeJabatan=2500000
    #     else:
    #         print("jabatan salah")
    #         return None
    #     if uangLembur!=None:
    #         total=feeJabatan+gajiPokok+uangLembur
    #     else:
    #         total=feeJabatan+gajiPokok
    #     print("total gaji {} adalah {}".format(self.username,total))

    
    




