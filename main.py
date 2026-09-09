class AksesServer:

    total_koneksi_aktif = 0

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        AksesServer.total_koneksi_aktif += 1

    @staticmethod
    def validasi_ip(ip_address):
        return ip_address.startswith("192.168.")
        # if ip_address.start() == "192.168.":
        #     return True
        # else:
        #     return False

    @classmethod
    def dari_string(cls, input):
        input_baru = input.split("-")
        return cls(input_baru[0], input_baru[1])
    
    @property
    def password(self):
        pass

    @password.getter
    def password(self):
        return "*** TERENKRIPSI ***"
    
    @password.setter
    def password(self, input):
        if len(input) < 8:
            print("Error: Password baru harus minimal 8 karakter!")
        else:
            self.__password = input
            print("Password berhasil diperbarui.")

    @password.deleter
    def password(self):
        self.__password = None
        AksesServer.total_koneksi_aktif -= 1
        print(f"Akses untuk user {self.username} telah dicabut. Password dihapus.")

# Skenario Pengujian (Dilarang mengubah kode di bawah ini)
print("--- UJI STATIC METHOD ---")
print(f"IP 192.168.1.10 valid? {AksesServer.validasi_ip('192.168.1.10')}")
print(f"IP 10.0.0.5 valid? {AksesServer.validasi_ip('10.0.0.5')}")

print("\n--- UJI CLASS METHOD & INSTANSIASI ---")
user1 = AksesServer("mahdi", "rahasia123")
user2 = AksesServer.dari_string("thoriq-sandi456")
print(f"Total koneksi aktif: {AksesServer.total_koneksi_aktif}")

print("\n--- UJI GETTER & SETTER PROPERTY ---")
print(f"Password {user1.username}: {user1.password}")
user1.password = "pendek"
user1.password = "passwordBaru99"
print(f"Password {user1.username} setelah diubah: {user1.password}")

print("\n--- UJI DELETER PROPERTY ---")
del user2.password
print(f"Total koneksi aktif sekarang: {AksesServer.total_koneksi_aktif}")