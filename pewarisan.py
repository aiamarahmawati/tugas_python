class Hewan:
    def __init__(self, nama):
        self.nama= nama
    def suara(self):
        print("Hewan bersuara")
        
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama}: Meong")
        
class Sapi(Hewan):
    def suara(self):
        print(f"{self.nama}: Moooo")
        
class Domba(Hewan):
    def suara(self):
        print(f"{self.nama}: Mbeee")
        
h = Hewan("nama")
h.suara()
k = Kucing("kucing")
k.suara()
s = Sapi("sapi")
s.suara()
d = Domba("domba")
d.suara()