# method resolution order || multiple inheritance

class A:

    def show(self):
        print("ini adalah method A")

class B:

    def show(self):
        print("ini adalah method B")

class C(A,B): # maka urutan prioritasnya adalah C > A > B

    # def show(self):
    #    print("ini adalah method C")
    pass

objek = C()
objek.show()
help(objek) # fungsi untuk melihat urutan prioritas / eksekusi inheritance

