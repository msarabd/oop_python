# diamond problem (A -> B, C -> D)

class A:

    def show(self):
        print("ini adalah method A")

class B(A):
    pass
    # def show(self):
    #     print("ini adalah method B")

class C(A):
    pass
    # def show(self):
    #     print("ini adalah method C")

class D(B,C):
    pass
    # def show(self):
    #     print("ini adalah method D")
    

objek = D()
objek.show()
help(objek)