class rekeningbank:
    def __init__(self, saldo):
        self.__saldo = saldo #private attribute
    def melihat(self):
        print(f"saldo anda {self.__saldo}")
    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah
        print(f"saldo anda ditambah {jumlah}")
        
r = rekeningbank(200000)
r.melihat()
r.tambah_saldo(100000)
r.melihat