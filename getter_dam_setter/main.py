class Pekerja:
    __jumlah = 0

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        # self.info = "name {} salary: \n\t {}".format(self.name, self.__salary) ini tidak akan bisa disettin di luar class, dia hanya berubah saat di awal saja (init)

    # sekarang method berlaku seperti instance variable
    @property
    def info(self):
        return "name {} salary: \n\t {}".format(self.name, self.__salary)

    @property # ini sebenarnya adalah getter juga, jadi kalau udh ada ini tidak perlu ada @method.getter
    def salary(self):
        pass

    @salary.getter
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, input):
        self.__salary = input

    @salary.deleter
    def salary(self):
        print(self.name, "dihapus")
        self.__salary = None

andi = Pekerja("andi", 80000)
print("== merubah info ==")
print(andi.info)
andi.name = "budi"
print(andi.info)

# print(andi.salary) akan muncul none, karena dia mengakses method salary bukan private variable nya (sebelum ada salary.getter)
print(andi.salary)
# andi.salary(50) ini kalau tidak pakai property setter, dia disetting menggunakan method
andi.salary = 50 # kita menyetting lewat method, dengan property setter
print(andi.salary)

del andi.salary
print(andi.salary)
