# from random import randint
# import player as player 

# fSword = s.Sword("Starter Sword", 20, "Starter", "Common", 100)
# Sword2 = s.Sword("Dagger", 76, "GODDDDDD", "GOD", 10000)

# print(Sword2)

# fSword.damage = 15

# print(fSword)

from random import randint
import player as playa

print('Welcome to the Adventures of Dillon. First we need you to pick a class.')
print('The classes are Berserk: Where you get a sword that does 30 damage, 5 speed, and an ability that lets you deal 2x damage for 3 turns.')
print('Mage: Where you get a staff that does 25 damage, 10 speed, and an ability that lets you set the enemy on fire, dealing 5 damage until either them or you are dead.')
print('Rogue: Where you get a dagger that does 15 damage, 45 speed, and an ability that lets you dodge the enemy attacks')
print('Archer: Where you get a bow that does 20 damage, 8 speed, and an ability that lets you shot 2 arrows at once with your bow fully charged back')

classInt = int(input('So what will it be. 1 for Berserk, 2 for Mage, 3 for rogue, or 4 for archer '))
if classInt == 1:
    Player = playa

