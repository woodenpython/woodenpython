import random as r

class player:
    health = 100
    health_max = 100
    inventory = []
    showinventory = []
    position = None
    inv_max = 8
    def __init__(self):
        self.name = str(input('Please enter the survivor\'s name:'))

    def search(self):
        while 1:
            print(self.position.showresouce)
            temp = input('Which would you like to take?\nEnter \'n\' to cancel:')
            if temp == 'n':
                break
            elif len(self.inventory) == self.inv_max:
                print('Inventory full!')
            else:
                self.inventory.append(self.position.resouce[int(temp)])
                self.updatainventory()
                del self.position.resouce[int(temp)]
                self.position.updatashowres()

    def battle(self):
        print('There are ' + str(len(self.position.enemy)) + ' zombies in the room.')
        #not complete


    def openpack(self):
        while 1:
            print(self.showinventory)
            a = int(input('Select one item:'))
            action = input('What would you like to do with it?\n1:Use 2:Combine 3:Abandon 4:Cancel')
            if action == '1':
                self.inventory[a].usemed(self)
                self.updatainventory()
            elif action == '2':
                b = int(input('Select another one:'))
                self.inventory[a].combine(self.inventory[a],self.inventory[b],self.inventory)
                self.updatainventory()
            elif action == '3':
                del self.inventory[a]
                self.updatainventory()
            print(self.showinventory)
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


class room:
    door = []
    resouce = []
    showresouce = []
    enemy = []
    special = []
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name

    #direction = [north,south,west,east]:1 or 0
    def gen_door(self,direction,doors):
        for i in range(4):
            if direction[i]:
                self.door.append(doors[i])
            else:
                self.door.append(0)

    def updatashowres(self):
        for item in self.resouce:
            self.showresouce.append(item.name)

    def gen_res(self):
        for x in range(3):
            a = r.randint(10)
            if a < 5:
                grass = Greenroot()
                self.resouce.append(grass)
                self.updatashowres()
            elif a < 7:
                grass = Redroot()
                self.resouce.append(grass)
                self.updatashowres()

    def gen_enemy(self):
        for x in range(3):
            b = r.randint(10)
            if b > x + 6:
                zman = zombie()
                self.enemy.append(zman)
        pass

class zombie:
    health = 100
    notice = 3

class Key:
    name = 'a fansy key'

class Door:
    one_side = 0
    lock = 0
    key = Key()

    def __init__(self,room1,room2):
        self.side1 = room1
        self.side2 = room2

    # return 1 for this door can be used
    def usedoor(self,player):
        if self.lock == 1:
            print('You need a key to open the door!')
            if self.key in player.inventory:
                a = input('Use your key?(y/n)')
                if a == 'y':
                    player.inventory.remove(self.key)
                    player.updatainventory()
                    return 1
            return 0
        if self.one_side == 1 and player.position == self.side1:
            print('Can not open the door from this side!')
            return 0
        if self.one_side == 1 and player.position == self.side2:
            print('You opened this door!')
            self.one_side = 0
            return 1
        return 1


#create game map
start = room(0,0,'Hiding Carbet')
passage = room(0,1,'Passage')
gunstorage = room(-1,1,'Weapon Locker')
storage1 = room(1,2,'Storage')


if __name__ == '__main__':
    print('Start new game...')
    tom = player()
    print('Find the exit!')


