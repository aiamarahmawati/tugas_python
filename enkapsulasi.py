class Buku:
    def __init__(self, judul, penulis):
        self.__judul = judul # private attribute
        self.penulis = penulis
        
    def info(self):
        print(f"judul: {self.__judul}, penulis: {self.penulis}")
        
b1 = Buku("python dasar", "budi")
b1.info()