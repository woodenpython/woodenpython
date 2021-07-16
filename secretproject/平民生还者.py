import random as r

'''
平民生还者ver0.0.1
本游戏中平民只能收集药草，只需存活20天
'''


class player:
    health = 100
    inventory = []
    showinventory = []
    def __init__(self):
        self.name = str(input('Please enter the survivor\'s name:'))

    def search(self):
        a = r.randint(0,10)
        if a > 4:
            print(self.showinventory)
            take = input('You found a green root, take or not?(y,n)')
            if take == 'n':
                pass
            elif take == 'y' and len(self.inventory) < 5:
                greenroot = Greenroot()
                self.inventory.append(greenroot)
                self.updatainventory()
            else:
                print('Inventory full!')

        b = r.randint(0,10)
        if b > 7:
            print(self.showinventory)
            take = input('You found a red root, take or not?(y,n)')
            if take == 'n':
                pass
            elif take == 'y' and len(self.inventory) < 5:
                redroot = Redroot()
                self.inventory.append(redroot)
                self.updatainventory()
            else:
                print('Inventory full!')

        c = r.randint(0,100)
        if c > 55:
            print('You are bitten by a zombie!')
            self.health -= r.randint(30,40)
            print('You health:',self.health)

    def openpack(self):
        while 1:
            print(self.showinventory)
            a = int(input('Select one item:'))
            action = input('What would you like to do with it?\n1:Use 2:Combine 3:Cancel')
            if action == '1':
                self.inventory[a].usemed(self)
                self.updatainventory()
            elif action == '2':
                b = int(input('Select another one:'))
                self.inventory[a].combine(self.inventory[a],self.inventory[b],self.inventory)
                self.updatainventory()
            con =input('Close the pack?(y/n)')
            if con == 'y':
                break

    def updatainventory(self):
        self.showinventory = []
        for each in self.inventory:
            self.showinventory.append(each.name)



class Medcine:
    name = ''
    value = 0
    def usemed(self,player):
        if self not in player.inventory:
            print('You don\'t have this!')
        else:
            player.inventory.remove(self)
            player.health += self.value
            if player.health > 100:
                player.health = 100
            print('Your health is '+str(player.health))

    def combine(self,one,another,inventory):
        if self.name == 'greenroot' and another.name == 'greenroot':
            print('Unable to combine!')
        elif self.name == 'redroot' and another.name == 'redroot':
            print('Unable to combine!')
        else:
            inventory.remove(one)
            inventory.remove(another)
            r_groot = R_Groot()
            inventory.append(r_groot)

class Greenroot(Medcine):
    name = 'greenroot'
    value = 20

class Redroot(Medcine):
    name = 'redroot'
    def usemed(self,player):
        print('You can\'t use it directly!')

class R_Groot(Medcine):
    name = 'r_groot'
    value = 50

print('Start new game...')
tom = player()
print('Survive 20 days to win!')
for i in range(0,20):
    print('\nThis is Day '+str(i+1))
    x = input('Ready to search?(y/n)')
    if x == 'n':
        tom.openpack()
    else:
        tom.search()
        i += 1
    print('You health at the end of the day:'+str(tom.health))
    if tom.health <= 0:
        print('\nYOU ARE DEAD')
        break
else:
    print('\nYOU SURVIVED!')



