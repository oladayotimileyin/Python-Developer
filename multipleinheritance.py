class user():
    def sign_in (self):
        print("logged in")

class wizard(user):
    def __init__(self, name,power):
        self._name = name
        self._power = power
    
    def attack(self):
        print(f"attacking with power {self._power}")

class archer(user):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows
    
    def attack(self):
        print(f"attacking with arrows: arrows left - {self._num_arrows}")

class hybrid(wizard, archer):
    def __init__(self, name, power, num_arrows):
        wizard.__init__(self, name, power)
        archer.__init__(self, name, num_arrows)

hb1 = hybrid("hybrid", 50, 100)

print(hb1._name)
print(hb1._power)
print(hb1._num_arrows)
print(hb1.sign_in())
