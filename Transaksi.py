

class Karyawan:
    __jumlahKaryawan=0
    
    def __init__(self,nama,totalGaji):
        Karyawan.__jumlahKaryawan+=1
        self.totalFee=0
        self.jumlahAbsensi=0
        self.nama=nama
        self.totalGaji=totalGaji
        
    def setTotalFee(self,fee):
        self.totalFee+=fee
        self.setGaji(fee)
 
    def setGaji(self,fee):
        self.totalGaji+=fee
        
    def showInfo(self,nama,totalGaji):
        print ("berikut Informasi")
        

class Order:
    def __init__(self,nama,total,namaKaryawan):
        self.nama=nama
        self.total=total
        
        namaKaryawan.setTotalFee(total)
        
class Transaksi:
    def __init__(self,orderDate,totalTransaksi,listIdBarang):
    

class Barang:
    idBarang=0
    def __init__(self,namaBarang,harga,keuntungan,jumlahStok):
        self.namaBarang=namaBarang
        self.harga=harga
        self.keuntungan=self.harga*keuntungan
        self.jumlahStok=jumlahStok
        self.jumlahTerjual=0
        
    def totalKeuntungan(self):
        total=self.jumlahTerjual*self.keuntungan
        return total
    
    def setJumlahStok(self):
        self.jumlahStok-=1
        
    def setJumlahTerjual(self):
        self.jumlahTerjual-=1
        self.setJumlahStok()
        self.totalKeuntungan()
        
         

    
tono=Karyawan("tono",300)
sri=Order("sri",500,tono)

print(tono.totalGaji)
# print(tono.__dict__)
    
    