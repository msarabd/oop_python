class Pekerja:
    """
    enkapsulasi
    1. mengubah semua variable menjadi private
    2. getter (untuk mengakses variable) dan setter (untuk setting variable)
    tujuannya agar variable tidak mudah mengalami perubahan yang tidak disengaja dan membuat variable lebih sedikit (akses di luar class)
    """
    def __init__(self, name, salary, allowance):
        self.__name = name
        self.__salary = salary
        self.__allowance = allowance

    # contoh getter
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary
    
    # contoh setter
    def dipotong(self, besarPotongan):
        self.__salary -= besarPotongan

chiko = Pekerja("chiko", 100000, 200)

# print(chiko.__name) akan error karena atribut name adalah private variable
print(chiko.getName())

# chiko.__salary = 300000 ini tidak akan mengubah atribut salary pada instance variable, tapi malah akan menambah variable baru
# print(chiko.__dict__)

chiko.dipotong(50000)
print(chiko.getSalary())