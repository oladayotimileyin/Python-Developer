# OOP
class PlayerCharacter:
    ##Class Object attribute are static unlike theother attributes
    #  - it does not change across instances
    membership = True
    def __init__(self, name, age): #self refer to the player character
        if (PlayerCharacter.membership):
            self.name = name ##attributes
            self.age = age

    def run(self):
        print(f'Runn far away {self.name}')
        return 'I am running!!'

    def talk(self):
            print(f'Hi, my name is {self.name}')
            return 'I am running!!'
    
player1 = PlayerCharacter("Timmy", 31)
player2 = PlayerCharacter('Noni', 20)


print(player1.name)
print(player2.age)
print(player1.run())
print(player1.talk())

print(player1.membership)

#help(player1)