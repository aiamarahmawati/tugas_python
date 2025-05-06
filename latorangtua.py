class Ayah:
    sifat = "egois"
    warna_kulit = "sawo matang"
    tinggi_badan = "167cm "
    def ayah(self):
        print("sifat ayah saya adalah egois")
        
class Ibu:
    watak = "gampang marah"
    warna_kulit = "sawo matang"
    tinggi_badan = "147cm"
    def ibu(self):
        print("sifat ibu saya adalah gampang marah")
        
class Ai(Ayah, Ibu):
    def karakternya(self):
        print(f"sifat yang diwariskan ayah saya kepada saya adalah sifat {self.sifat} dan ibu saya mewariskan sifat {self.watak}")
        
class kaka(Ayah, Ibu):
    def turunan(self):
        print(f"ayah saya mewariskan sifat {self.sifat} dan ibu saya mewariskan sifat {self.watak}")
        
a = Ayah()
a.ayah()

i = Ibu()
i.ibu()

a1 = Ai()
a1.karakternya()

k = kaka()
k.turunan()