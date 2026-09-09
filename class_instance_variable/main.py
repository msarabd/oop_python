class Hero: # template
    # static variable (nempel ke class)
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputAttack):
        # instance variable (nempel ke object)
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        Hero.jumlah += 1
        print("Menambahkan hero dengan nama ", inputName)


hero1 = Hero("Sniper", 200, 100)
print(Hero.jumlah)
hero2 = Hero("Rusher", 150, 250)
print(Hero.jumlah)
hero3 = Hero("Bomber", 180, 150)
print(Hero.jumlah)