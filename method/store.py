import sqlite3


databaseName='databaseBranch.it.db'
conn = sqlite3.connect(databaseName)


class Toko ():
    __cabangDict={}
    @classmethod
    def getIdCabang(cls,cabang):
        cabang=str(cabang)
        return Toko.__cabangDict[cabang]

    @classmethod
    def getCabangDict(cls):
        return Toko.__cabangDict

    @classmethod
    def getCabangbyId(cls,id):
        a=Toko.__cabangDict
        key_list = list(a.keys())
        val_list = list(a.values())
        position=val_list.index(id)
        return key_list[position]
    
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

    def setOmset(self,tambahOmset):
        self.omset+=tambahOmset
        data=conn.cursor().execute("update toko set omset=? where idCabang=?",(self.omset,self.idCabang,))
        conn.commit()

    def tampilkanInfo(self):
        data=conn.cursor().execute("select * from user").fetchall()
        id=0
        for row in data:
            # print(row[0][0])
            # print (self.idCabang,"j==")
            if row[0][0]==str(2) and row[0][5]==str(self.idCabang):
                id=row[0]
                print(id)
                break

        a=conn.cursor().execute("select username from user where idUser=?",(id,)).fetchall()
        namaManager=None
        for row in a:
            namaManager=row[0]

        print("""
            Nama Toko \t : Cabang {}
            Manager Toko : {}
            Omset Toko \t : Rp {} ,-
        """
        .format(self.namaCabang,namaManager,self.omset))


