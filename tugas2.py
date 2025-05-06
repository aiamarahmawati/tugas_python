class karyawan:
    def __init__(self, nama):
        self.nama = nama
    def info(self):
        print (f"Halo saya karyawan bernama {self.nama}")
class manajer(karyawan):
    def info(self):
        print (f"Halo saya {self.nama} sebagai manajer")
        
d1 = karyawan("ama")
d1.info()
d1 = manajer("ama")
d1.info()