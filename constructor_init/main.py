class Hero: # template

     def __init__(self, inputName, inputHealth, inputAttack):
          self.name = inputName
          self.health = inputHealth
          self.attack = inputAttack

     
hero1 = Hero("Sniper", 200, 100)
hero2 = Hero("Rusher", 150, 250)
hero3 = Hero("Bomber", 180, 150)

print(hero1.name)
print(hero2.health)
print(hero3.attack)
print(hero1.__dict__)
