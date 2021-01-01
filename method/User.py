import sqlite3

from .store import Toko
databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

conn.execute("DROP TABLE IF EXISTS user")
conn.execute("CREATE TABLE IF NOT EXISTS user  (idUser int primary key,username text ,password text, jumlahAbsensi int ,  totalGaji int)")

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

class Owner(User):
    __jumlahOwner=1
    
    @classmethod  #agar method nempel di class bukan di object 
    def listStatus(cls,idStatus): #override method listStatus yang ada di user
        None
    
    def __init__(self,username,password,cabang,status):
        super().__init__(username,password,cabang,"Owner")
        self.__password=password
        self.idJabatan=str(1).zfill(1)
        self.idStatus=str(0).zfill(2)
        self.idCabang=str(0).zfill(2)
        self.id =str(Owner.__jumlahOwner).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
    def showInfo(self):
        print("username : {} /n Jabatan : {} /n Status : {}".format(self.username,self.jabatan,self.status))

    
    
class Karyawan(User) :
    __jumlahKaryawan=0
    __statusDict = {"Karyawan Tetap": 1,"Karyawan Tidak Tetap": 2,"Karyawan Magang":3}
    @classmethod  #agar method nempel di class bukan di object 
    def listStatus(cls,status): #override method listStatus yang ada di user
        idStatus=str((Karyawan.__statusDict[status])).zfill(2)
        return idStatus

    @classmethod  #agar method nempel di class bukan di object 
    def listGajiPokok(cls,idStatus): #override method listStatus yang ada di user
        gajiPokokDict={1:1500000,2:1000000,3:500000}
        gajiPokok=gajiPokokDict[int(idStatus)]
        return gajiPokok
    @classmethod
    def getStatusDict(cls)
        return Karyawan.__statusDict
    
    def __init__(self,username,password,cabang,status):
        Karyawan.__jumlahKaryawan+=1
        super().__init__(username,password,cabang,status)
        self.__username=username
        self.__password=password
        self.idJabatan= str(3).zfill(1)
        self.id =str(Karyawan.__jumlahKaryawan).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        self.totalGaji=self.listGajiPokok(self.idStatus)
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
    def showInfo(self):
        print("username : {} /n Jabatan : {} /n Status : {}".format(self.username,self.jabatan,self.status))


class Manager(User) :

    __jumlahManager=0
    
    def __init__(self,username,password,cabang,status):
        Manager.__jumlahManager+=1
        super().__init__(username,password,cabang,status)
        self.__username=username
        self.__password=password
        self.idStatus=str(1).zfill(2)
        self.idJabatan= str(2).zfill(1)
        self.id =str(Manager.__jumlahManager).zfill(3)
        self.idUser=str(self.idJabatan) +"-"+ str(self.idStatus) +"-"+ str(self.idCabang)+"-"+ self.id
        self.totalGaji=2500000
        conn.execute("insert or ignore into user values (?,?,?,?,?)" , (self.idUser,self.username,self.__password,self.jumlahAbsensi,self.totalGaji)) #masukkan ke database
        conn.commit()
        
        
    def showInfo(self,username,status,jabatan):
        print("username : {} /n Status : {} /n Jabatan : {}".format(self.username,self.status,self.jabatan))


# amiroh1=Karyawan("woy2","12345678","Jember","Karyawan Tetap",)
# amiroh2=Manager("woyy","12345678","Green Hill","Karyawan Magang",)
# amiroh2.setTotalFee(2000000)
# amiroh2.setJumlahAbsensi()
# print(amiroh.idUser)