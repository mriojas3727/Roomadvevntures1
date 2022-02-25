#Name: Matthew Riojas
#Date: 2/17/2022
#Description: Room adventures
import time
from thedeath import *

#blueprint
class Room(object):
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value
    
    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)

    def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

    def addGrabbable(self, item):
        self._grabbables.append(item)

    def delGrabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        s = "You are in {}.\n".format(self.name)

        s += "You see: "
        for item in self.items:
            s+= item + " "
        s += "'\n"

        for exit in self.exits:
            s += exit + " "
        
        return s

def createRooms():
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    r1.addExit("east" , r2)
    r1.addExit("south" , r3)
    r1.addGrabbable("key")
    r1.addItem("chair" , "It is made of wicker and no one is sitting on it.")
    r1.addItem("table" , "It is made of oak. A golden key rests on it")

    r2.addExit("west" , r1)
    r2.addExit("south" , r4)
    r2.addItem("rug" , "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace" , "it is full of ashes.")
    
    r3.addExit("north" , r1)
    r3.addExit("east" , r4)
    r3.addGrabbable("book")
    r3.addItem("bookshelves" , "They are empty. Go figure.")
    r3.addItem("statue" , "There is nothing special about it.")
    r3.addItem("desk" , "The statue is resting on it. SO is a book.")

    r4.addExit("north" , r2)
    r4.addExit("west" , r3)
    r4.addExit("south" , None)
    r4.addGrabbable("6-pack")
    r4.addItem("soda_making_machine" , "Gourd is making some sort of soda on the soda making machine.A 6-pack is resting beside it.")
    global currentRoom
    currentRoom = r1
    









##START GAME

inventory = []
createRooms()

while True:
    
        status = "{}\n You are carrying: {}\n".format(currentRoom, inventory)
        if(currentRoom == None):
            death()
            status = "You are dead."
            print(status)
            break
        print("=========================================================")
        print(status)
        action = input("What to do? ")
        action.lower()
        if(action == "quit" or action == "exit" or action == "bye"):
            break
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
        words = action.split()
        if(len(words) == 2):
            verb = words[0]
            noun = words[1]

            if(verb == "go"):
                response = "invalid exit."
                for i in range(len(currentRoom.exits)):
                    
                    if(noun == currentRoom.exits[i]):
                        currentRoom = currentRoom.exitLocations[i]
                    
                        response = "Room changed."
                        break
            elif(verb =="look"):
                response = "I dont see that item."

                for i in range(len(currentRoom.items)):
                    if(noun == currentRoom.items[i]):
                        response = currentRoom.itemDescriptions[i]

                        break

            elif(verb == "take"):
                response = "I don't see that item."

                for grabbable in currentRoom.grabbables:
                    if(noun == grabbable):
                        inventory.append(grabbable)

                        currentRoom.delGrabbable(grabbable)

                        response = "Item grabbed."

                        break
        

        print("\n{}".format(response))
        time.sleep(2)