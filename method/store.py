import sqlite3


databaseName='iniDBbuatCoba.db'
conn = sqlite3.connect(databaseName)

conn.execute("DROP TABLE IF EXISTS toko")
conn.execute("CREATE TABLE IF NOT EXISTS toko (idCabang int primary key,namaCabang text ,omset int)")

class Toko ():
    __cabangDict={}
    @classmethod
    def getIdCabang(cls,cabang):
        return Toko.__cabangDict[cabang]
    
    @classmethod  #agar method nempel di class bukan di object 
    def addListCabang(cls,cabang): 
        Toko.__cabangDict[cabang]=len(Toko.__cabangDict)+1
        return Toko.__cabangDict[cabang]
    
    def __init__(self,cabang):
        self.namaCabang=cabang
        self.idCabang=len(Toko.__cabangDict)+1
        self.omset=0
        Toko.addListCabang(cabang)
        conn.execute("insert or ignore into toko values (?,?,?)" , (self.idCabang, self.namaCabang, self.omset))#masukkan ke database
        conn.commit()

    def setOmset(tambahOmset):
        self.omset+=tambahOmset
        data=conn.cursor().execute("update toko set totalGaji=? where idUser=?",(self.totalGaji,self.idUser,))
        conn.commit()

# Sukodono=Toko("Sukodono")
# a=Toko.getCabangDict()
# print(a)
# Madiun=Toko("Madiun")
# Madiunn=Toko("Madiunm ")
# b=Toko.getCabangDict()
# print(b)

# print(Sukodono.idCabang)