class laptop:
    def __init__(self, merk, ram):
        self.merk = merk
        self.ram = ram
    def info(self):
        print(f"Laptop ini bermerek {self.merk} dengan {self.ram}")
        
laptop_saya = laptop("Asus", "RAM 8GB")
laptop_saya.info()