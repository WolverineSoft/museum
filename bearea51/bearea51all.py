# Ported to the web in 2025 by Ravi Bhatt

class Room(object):
    def __init__(self):
        self.items = []
        self.bears = []
        self.paths = {}
        self.desc = ""
        self.name = ""
        self.first = True
        self.num = 0

    def move(self, path):
        if len(self.bears) == 0:
            if path in self.paths:
                return self.paths[path]
            else:
                print("  You hit your head on the wall.")
                return self.num
        else:
            print("  You can't do that with bears around.")
            return self.num

    def take(self, item):
        if len(self.bears) == 0:
            if item in self.items:
                print("You got the " + item)
                self.items.remove(item)
                return item
            print("Item isn't here.")
        else:
            print("  You can't do that with bears around.")

    def use(self, thing):
        pass
    
    def Items(self):
        if len(self.items) == 0:
            return ""

        stuff = "\nItems: "

        for item in range(len(self.items)):
            if len(self.items) == 1:
                stuff = stuff + self.items[item] + "(1)"
            elif item < len(self.items) - 1:
                stuff = stuff + self.items[item] + "(" + str(item + 1) + "), "
            else:
                stuff = stuff + "and " + self.items[item] + "(" + str(item + 1) + ")"

        return stuff + "."

    
    def Paths(self):
        if len(self.paths) == 0:
            return "\nNo way out."

        ways = "\nPaths: "
        
        for path in range(len(self.paths)):
            if 1 == len(self.paths):
                ways = ways + self.paths[path] + "(1)"
            elif path < len(self.paths) - 1:
                ways = ways + self.paths[path] + "(" + str(path + 1) + "), "
            else:
                ways = ways + "and " + self.paths[path] + "(" + str(path + 1) + ")"

        return ways + "."

    def Bears(self):
        if len(self.bears) == 0:
            return ""

        fauna = "\nBears: "
        
        for bear in range(len(self.bears)):
            if 1 == len(self.bears):
                fauna = fauna + self.bears[bear].name + "(1)"
            elif bear < len(self.bears) - 1:
                fauna = fauna + self.bears[bear].name + "(" + str(bear + 1) + "), "
            else:
                fauna = fauna + "and " + self.bears[bear].name + "(" + str(bear + 1) + ")"

        return fauna + "."
    
    def info(self):
        return "\n" + self.desc + self.Paths() + self.Items() + self.Bears()  + "\n"
        
    def brief(self):
        state = self.name + self.Paths()

        if len(self.items) > 0:
            state = state + self.Items()
        if len(self.bears) > 0:
            state = state + self.Bears()
            
        return "\n" + state + "\n"

import random

class Bear(object):
    def __init__(self, kind):
        self.kind = kind
        
        if kind == "black":
            self.hp = 10
            self.bite = 2
            self.paw = 2
            self.name = self.kind + " bear"
        elif kind == "grizzly":
            self.hp = 20
            self.bite = 6
            self.paw = 8
            self.name = self.kind + " bear"
        elif kind == "polar":
            self.hp = 30
            self.bite = 10
            self.paw = 8
            self.name = self.kind + " bear"
        else:
            self.hp = 100
            self.bite = 15
            self.paw = 15
            self.name = self.kind + " Bear"

    def attack(self):
        if random.randint(0,1) == 0:
            return self.bite + random.randint(-self.bite //2, self.bite //2), "bite"
        else:
            return self.paw + random.randint(-self.paw //4, self.paw //4), "paw"
        
    def attacked(self, damage):
        self.hp -= damage
    
    def heal(self):
        if self.kind == "black":
            self.hp = 10
        elif self.kind == "grizzly":
            self.hp = 20
        elif self.kind == "polar":
            self.hp = 30
        else:
            self.hp = 100

class CentralComputer():
    @staticmethod
    def play(difficulty = 3):
        q1 = ": "
        q2 = ": "
        q3 = ": "
        q4 = ": "
        q5 = ": "
        
        wrong = 0
        
        if difficulty <= 0:
            print("'Eh, I'm drained. Thanks for playing with me! Here's the card.")
            return True
        elif difficulty == 1:
            q1 = "-chair\n-twelve\n-Blue\n: "
            q2 = "-toothbrush\n-otter\n-echo\n: "
            q3 = "-time\n-phone\n-firetruck\n: "
            q4 = "-athlete\n-nose\n-book\n: "
            q5 = "-True\n-False\n: "
        elif difficulty == 2:
            q1 = "-three\n-twelve\n-four\n: "
            q2 = "-phone\n-bird\n-echo\n: "
            q3 = "-time\n-religion\n-authority\n: "
            q4 = "-soldier\n-nose\n-lawyer\n: "
            q5 = "-True\n-False\n: "


        print("'I am lonely. Will you play with me? If you win, I'll give you a magnetic card!.")
        
        play = input("'Play with me?' ")
        play = play.lower()[0]

        if play != 'y':
            print("'*sniff* :('")
            return False

        print("'Yay! Okay, here are the rules: I'll ask you 5 riddles, and if you can\nanswer enough correctly, you win!'")
        print("'Ready? Okay.'")
        
        print("'1. How many three cent stamps are in a dozen?'")
        answer = input(q1)
        answer = answer.lower()

        if answer == "twelve" or "12":
            print("'That one was easy. Let's move on!'")
        else:
            wrong += 1
            print("'Oh, I'm sorry. Better luck on this next one!")

        print("'2. You heard me before, Yet you hear me again, Then I die, 'Till you call\nme again. What am I?'")
        answer = input(q2)
        answer = answer.lower().split()

        if "echo" in answer:
            print("'Aw, good job! Let's see if we can't trip you up...'")
        else:
            wrong += 1
            print("'Ouch. That was the wrong answer.'")

        print("'3. Mountains will crumble and temples will fall, and no man can survive\nits endless call. What is it?'")
        answer = input(q3)
        answer = answer.lower().split()

        if "time" in answer:
            print("'Ooh, nice! How's this?'")
        else:
            wrong += 1
            print("'Well, that one was kinda tough.'")

        print("'4. I can run but not walk. Wherever I go, thought follows close behind.\nWhat am I?'")
        answer = input(q4)
        answer = answer.lower().split()

        if "nose" in answer:
            print("'Wow! That was a toughy! Okay, here's the last one:'")
        else:
            wrong += 1
            print("'Don't worry, I got it wrong the first time I was asked it.'")

        print("'5. True or False: The Little Penguin is the world's smallest of all\npenguin species?'")
        answer = input(q5)
        answer = answer.lower()

        if answer == 1 or 't' or 'true':
            print("'Haha, nice! I hold a grudge against that particular one, but that's\nanother story.'")
        else:
            wrong += 1
            print("'Oh, I'm sorry, but that was wrong.'")

        if wrong > 1:
            print("'Aw, I'm sorry. I promise I'll go easier on you next time!'")
            return False
        print("'Aw, I'm sad to see you go. Oh well, a promise is a promise!'")
        
        return True

# beginning
class start(Room):
    def __init__(self):
        self.num = 0
        self.name = "Cave Exit"
        self.paths = {"north":1}
        self.desc = "Nighttime in the middle of the forest near the recently  collapsed exit\nfrom a cave system."
        self.bears = []
        self.items = []
        self.first = False

    def Paths(self):
        return "\nThere is a dim light visible to the North."

    def move(self, path):
        if path in self.paths:
            return self.paths[path]
        else:
            print("There is a lack of light. You are likely to be eaten by a  bear.")
            return self.num

# first bear 
class latrine(Room):
    def __init__(self):
        self.num = 1
        self.name = "Latrine"
        self.paths = {"west":2}
        self.desc = "A small clearing outside a large, hidden complex.\nThe  smell of bear dung is everywhere."
        self.bears = [Bear("black")]
        self.items = []
        self.first = True

    def Paths(self):
        return "\nThere is a door to the west"

    def info(self):
        return "\n" + self.desc + self.Paths() + self.Items() + self.Bears()  + "\n\nC: Type 'h' or 'hit' to hit the bear with your fists,\n  'k' or 'kick' to kick the bear with your feet.\n"
    
    def move(self, path):
        if len(self.bears) < 1:
            if path in self.paths:
                return self.paths[path]
            else:
                print("There is a lack of light. You are likely to be eaten by a bear.")
                return self.num
        else:
            print("You can't do that when bears are around.")
            return self.num

# first branch
class bearracks(Room):
    def __init__(self):
        self.num = 2
        self.name = "Bearracks"
        self.paths = {"north":-5,"south":3,"east":1,"west":4}
        self.desc = "A large room with many straw pile beds and other Ursonal  effects.\nIt seems as if most of the army has been mobilized elsewhere."
        self.bears = [Bear("black"),Bear("black")]
        self.items = []
        self.first = True

    def Paths(self):
        paths = "\nLatrine to the East, Mess Hall to the South, Pawmory to the  West,\nSouth Hall to the North."
        if self.paths["north"] < 0:
            paths = paths + "\nThe door to South Hall is locked.\nIf only you  had something durable with which to kick it down..."
        return paths

    def info(self):
        return "\n" + self.desc + self.Paths() + self.Items() + self.Bears()  + "\n\nC: Type 'h 1' to specifically the bear with the '1' next to its name.,\n  When bear 1 is dead, bear 2 will become bear 1, and so on.\n"

    def move(self, path):
        if len(self.bears) < 1:
            if self.paths["north"] == 5 or path != "north":
                if path in self.paths:
                    return self.paths[path]
                else:
                    print("  You hit your head against the wall.")
                    return self.num
            else:
                print("  The door holds steady against your head-banging.")
                return self.num
        else:
            print("You can't do that when bears are around")
            return self.num

    def use(self, item):
        if self.paths["north"] == -5 and item == "boots":
            self.paths["north"] = 5
            print()
            print("  The door to your kick is like logic to Bill O'Reilly")
            print("  You can now head North")
        else:
            print("  Item has no use here.")

# storagekey
class mess(Room):
    def __init__(self):
        self.num = 3
        self.name = "Mess Hall"
        self.paths = {"north":2}
        self.desc = "A large enough cafeteria, strewn with the bones of  eagles,\ndismembered children, and French Fries. Typical."
        self.bears = [Bear("grizzly")]
        self.items = ["storagekey"]
        self.first = True

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see something shiny sticking out of a pile of trash... (storagekey).\n\nC: Type 'take storagekey' to put it into your inventory, but  you'll have\nto take care of any bears in the area first."
        return ""
    
    def Paths(self):
        return "\nBearracks to the North."

# boots
class pawmory(Room):
    def __init__(self):
        self.num = 4
        self.name = "Pawmory"
        self.paths = {"east":2}
        self.desc = "A small chamber, filled from floor to ceiling with all  manner of\nhigh-grade ursine combat enhancers."
        self.bears = [Bear("black"),Bear("grizzly")]
        self.items = ["boots"]
        self.first = True
        
    def Paths(self):
        return "\nBearracks to the East."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see Reinforced Boots of Kicking, sitting in a corner  (boots)\nWith those, you'll kick harder\n\nC: Type 'take boots' to put the boots  in your inventory, but you'll have\nto take care of any bears in the area first.  There may be some instance\nwhere 'use boots' has an effect."
        return ""

# nothing special
class hallS(Room):
    def __init__(self):
        self.num = 5
        self.name = "South Hall"
        self.paths = {"north":11,"south":2,"east":-7,"west":-6}
        self.desc = "The Southern portion of a large hall.\nThe grimy floor  suggests that this end is more subject to menial labor."
        self.bears = [Bear("black"),Bear("grizzly"),Bear("black")]
        self.items = []
        self.first = True

    def Paths(self):
        paths = "\nBearracks to the South, Dungeon to the East, and Storage to  the West."
        if self.paths["east"] < 0:
            paths = paths + " The Dungeon is locked."
        if self.paths["west"] < 0:
            paths = paths + " The Storage room is locked."
        return paths

    def info(self):
            return "\n" + self.desc + self.Paths() + self.Items() + self.Bears()  + "\n\nC: Any keys you collect will be stored in your key set.  To see if any of your\nkeys will open any of these doors, enter 'use keys', and  if you have picked\nup the right key, the door will become unlocked.\n"
    
    def move(self, path):
        if len(self.bears) < 1:
            if self.paths["east"] == 7 or path != "east":
                if self.paths["west"] == 6 or path != "west":
                    if path in self.paths:
                        return self.paths[path]
                    else:
                        print("  You hit your head on the wall.")
                        return self.num
            print("  The door holds steady against your head-banging.")
            return self.num
        else:
            print("You can't do that with bears around")
            return self.num
    
    def use(self, item):
        if type(item) == list:
            if self.paths["west"] == -6 and "storagekey" in item:
                print("You unlocked Storage.")
                self.paths["west"] = 6
            elif self.paths["east"] == -7 and "dungeonkey" in item:
                print("You unlocked the Dungeon.")
                self.paths["east"] = 7
            else:
                print("You are missing the right key.")
        else:
            print("  Item has no use here.")

# shirt
class storage(Room):
    def __init__(self):
        self.num = 6
        self.name = "Storage"
        self.paths = {"east":5}
        self.desc = "A room full of the typical bear supplies: picanic baskets, jars of honey,\nexplicit magazines, satanic idols, a bust of Lennon, and Harry  Potter books."
        self.items = ["shirt"]
        self.bears = [Bear("black"),Bear("black"),Bear("black")]
        self.first = True

    def Paths(self):
        return "\nSouthern Hall to the East."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see the Chainmail Shirt of Innard Retention hanging  from the wall ('shirt').\nIt won't keep you warm in cold weather, but it'll  shield you from half the\ndamage caused by bear paws."
        return ""

# nothing special
class dungeon(Room):
    def __init__(self):
        self.num = 7
        self.name = "Dungeon"
        self.paths = {"north":10,"south":8,"east":9,"west":5}
        self.desc = "A filthy dungeon containing several cages. God only knows  what horrors\nthe prisoners are subjected too..."
        self.bears = [Bear("black"),Bear("polar"),Bear("black")]
        self.items = []
        self.first = True

    def Paths(self):
        return "\nA number of cages lie at the Northern, Southern, and Eastern  walls\nof the dungeon."

# captives
class cageS(Room):
    def __init__(self):
        self.num = 8
        self.name = "South Cage"
        self.paths = {"north":7}
        self.desc = "The cleanest cage, it seems this is where the newcomers  are first placed."
        self.bears = [Bear("polar")]
        self.items = ["captives"]
        self.first = True

    def Paths(self):
        return "\nRest of Dungeon to the North."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see a group of French prisoners (captives)."
        return ""

# captives
class cageE(Room):
    def __init__(self):
        self.num = 9
        self.name = "East Cage"
        self.paths = {"west":7}
        self.desc = "The floor is puddled with sweat. This must be where they  keep the\nprisoners good for manual labor."
        self.bears = [Bear("grizzly")]
        self.items = ["captives"]
        self.first = True

    def Paths(self):
        return "\nRest of Dungeon to West"

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see a ragged group of French prisoners (captives)."
        return ""

# captives
class cageN(Room):
    def __init__(self):
        self.num = 10
        self.name = "North Cage"
        self.paths = {"south":7}
        self.desc = "The floor here is other-puddled. This must be where the  feeble prisoners are\nleft to rot."
        self.bears = [Bear("black")]
        self.items = ["captives"]
        self.first = True

    def Paths(self):
        return "\nRest of Dungeon to West."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see a sickly group of French prisoners (captives)."
        return ""

# nothing special
class hallN(Room):
    def __init__(self):
        self.num = 11
        self.name = "North Hall"
        self.paths = {"north":-17,"south":5,"east":-12,"west":13}
        self.desc = "The Northern portion of the large Hall.\nIts cleaner state  indicates the higher status of those in this area."
        self.bears = [Bear("grizzly"),Bear("grizzly")]
        self.items = []
        self.first = True

    def Paths(self):
        paths = "\nSouthern Hall to the South, Nursery to the East, Lounge to  the West,\nand an outdoor area to the North leading to the Research Laboratory."
        if self.paths["east"] < 0:
            paths = paths + "\nThe Nursery is locked."
        if self.paths["north"] < 0:
            paths = paths + "\nA blizzard rages to the North. If only you had  something to keep you warm..."
        return paths

    def move(self, path):
        if len(self.bears) < 1:
            if self.paths["east"] == 12 or path != "east":
                if self.paths["north"] == 17 or path != "north":
                    if path in self.paths:
                        return self.paths[path]
                    else:
                        print("  You hit your head on the wall.")
                        return self.num
            if path == "north":
                print("  The raging blizzard drives you back indoors.")
            else:
                print("  The door holds steady against your head-banging.")
            return self.num
        else:
            print("You can't do that with bears around.")
            return self.num

    def use(self, item):
        if type(item) == list and self.paths["east"] == -12 and "nurserykey" in item:
            print("You unlocked the Nursery.")
            self.paths["east"] = 12
        elif self.paths["north"] == -17 and item == "scarf":
            print("You tighten the scarf around your neck, ready to go through  the blizzard")
            self.paths["north"] = 17
        else:
            print("  Item has no use here.")

# flag
class nursery(Room):
    def __init__(self):
        self.num = 12
        self.name = "Nursery"
        self.paths = {"west":11}
        self.desc = "A large room full of howling cubs, all either listening  to Rock,\nwatching Reality TV, or playing Murder Simulators.\nFortunately, they  are all safely harnessed, and cannot harm you."
        self.bears = [Bear("black"),Bear("black"),Bear("black"),Bear("black")]
        self.items = ["flag"]

        self.first = True

    def Paths(self):
        return "\nNorthern Hall to the West."

    def Items(self):
        if len(self.items) == 1:
           return "\nAn American flag is hanging in the center of the room so  the cubs\nwill associate Freedom with Wanton Violence (flag).\nLet the power of  the US fuel your strength and double your attack power"
        return ""

# nothing special
class lounge(Room):
    def __init__(self):
        self.num = 13
        self.name = "Lounge"
        self.paths = {"north":14,"south":16,"east":11,"west":15}
        self.desc = "A large, luxurious lounge connecting all the upper-level  Ursinel's quarters."
        self.bears = [Bear("polar")]
        self.items = []
        self.first = True

    def Paths(self):
        return "\nUrsaffers Quarters are to the North, the Alpha Male's to the  West,\nand the Growlfriends' to the South."

# dungeonkey
class ursaffers(Room):
    def __init__(self):
        self.num = 14
        self.name = "Ursaffers' Quarters"
        self.paths = {"south":13}
        self.desc = "A luxurious sleeping area for the more proven bears."
        self.bears = [Bear("grizzly"),Bear("grizzly"),Bear("black")]
        self.items = ["dungeonkey"]
        self.first = True

    def Paths(self):
        return "\nThe Lounge lies to the South."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see a key sitting on a dresser (dungeonkey)."
        return ""

# scarf
class alphaMale(Room):
    def __init__(self):
        self.num = 15
        self.name = "Alpha Male's Room"
        self.paths = {"east":13}
        self.desc = "The epitome of bear luxury, from cologne of children's  tears to eagle heads on the wall to people-skin rugs."
        self.bears = [Bear("black"),Bear("polar")]
        self.items = ["scarf"]
        self.first = True

    def Paths(self):
        return "\nThe Lounge is to the East."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see the Thick Scarf of Jugular Protection thrown over  a chair (scarf).\nDesigned to protect the neck from more than the cold, this  halves the damage done by bear bites"
        return ""

# nurserykey
class growlfriends(Room):
    def __init__(self):
        self.num = 16
        self.name = "Growlfriends' Quarters"
        self.paths = {"north":13}
        self.desc = "A simple, yet comfortable room, with bedding piles  composed of fine,\nspecially treated hay."
        self.bears = [Bear("black"),Bear("black"),Bear("black")]
        self.items = ["nurserykey"]
        self.first = True
        
    def Paths(self):
        return "\nThe Lounge is to the North."

    def Items(self):
        if len(self.items) == 1:
            return "\nYou see a key next to a bed pile (nurserykey)."
        return ""

# nothing special
class lab(Room):
    def __init__(self):
        self.num = 17
        self.name = "Rarsearch Laboratory"
        self.paths = {"south":11,"east":18,"west":-19}
        self.desc = "A large, complex lab equipped for genetic modification,  the equipment itself\nmodified to be used by bears.\nAn impenetrable blast door  has the symbol for Helipad painted above it."
        self.bears = [Bear("polar"),Bear("polar")]
        self.items = []
        self.first = True

    def Paths(self):
        paths = "\nThe Central Computer lies to the East, and the Test Chamber to  the West."

        if self.paths["west"] < 0:
            paths = paths + " The Test Chamber has been locked down by the  Central Computer.\nYou'll need a magnetic card to get through."
        return paths

    def use(self, item):
        if self.paths["west"] == -19 and item == "card":
            print("You unlocked the Test Chamber.")
            self.paths["west"] = 19
        else:
            print("  Item does nothing here.")

# computer and card
class comp(Room):
    def __init__(self):
        self.num = 18
        self.name = "Central Computer"
        self.paths = {"west":17}
        self.desc = "A gigantic computer is the only thing in this room. It  wants to be used (comp)."
        self.bears = []
        self.items = []
        self.first = True
        self.difficulty = 3

    def Paths(self):
        return "\nThe Rarsearch Laboratory is to the West."

    def use(self, item):
        if item == "comp":
            card = CentralComputer.play(self.difficulty)

            if card == False:
                self.difficulty -= 1
            else:
                print("A card has appeared out of a slot in the computer")
                self.items.append("card")
        else:
            print("  That item doesn't work here.")
            
# Prizzly Bear part 1
class test(Room):
    def __init__(self):
        self.num = 19
        self.name = "Test Chamber"
        self.paths = {"east":-20}
        self.desc = "A giant, empty tank sits in the middle of the room, all  manner of wires and\nmachines hooked up to it. The door to the lab is locked."
        self.bears = [Bear("Prizzly")]
        self.items = []
        self.first = True

    def Paths(self):
        if self.paths["east"] == 20:
            return "\nThere is a hole where the Prizzly Bear crashed through  \that leads\nonto the Helipad."
        return "There's no path out!"
    
    def move(self, path):
        if len(self.bears) < 1:
            if self.paths["east"] == 20:
                if path in self.paths:
                    return self.paths[path]
                else:
                    print(" You hit your head on the wall.")
                    return self.num
            else:
                return self.num
        else:
            print("You can't do that with bears around.")
            return self.num
    
    def crash(self):
        self.paths["east"] = 20
        self.bears.remove(self.bears[0])
        print("The enraged Prizzly Bear smashes through a wall to the East, \ntowards the Helipad!")

# Prizzly Bear part 2: endgame
class helipad(Room):
    def __init__(self):
        self.num = 20
        self.name = "Helipad"
        self.paths = {}
        self.desc = "An eagle sounds in the distance as the Prizzly Bear roars  mightily,\nstanding in the center of the Helipad."
        self.bears = [Bear("Prizzly")]
        self.items = []
        self.first = True

    def eagle(self):
        print("Suddenly, Stephen Jr. swoops out of the sky and drops a cross  in front of you!")
        self.items.append("cross")

    def take(self, item):
        if item == "cross":
            return "cross"
        else:
            print("There's nothing like that here.")

    def use(self, item):
        if item == "cross":
            self.bears.remove(self.bears[0])


class Level(object):
    def __init__(self):
        self.rooms = [start(),latrine(),bearracks(),mess(),pawmory(),hallS(),                       storage(),dungeon(),cageS(),cageE(),cageN(),hallN(),                       nursery(),lounge(),ursaffers(),alphaMale(),growlfriends(),                       lab(),comp(),test(),helipad()]
        
        self.room = self.rooms[0]
        self.prev = self.rooms[0]

    def move(self, path):
        result = self.room.move(path)

        if type(result) == None:
            return False
        
        self.prev = self.room
        self.room = self.rooms[result]
        
        if self.prev.num != self.room.num:
            if self.room.first != True:
                print(self.room.brief())
            else:
                print(self.room.info())
                self.room.first = False

            return True

    def retreat(self):
        if self.room.num != self.prev.num:
            if len(self.room.paths) > 0:
                self.room = self.prev
                print("  You send out a mist of Bear Spray and retreat back into the  \narea you came from.")
                print()
            else:
                print("Your escape route is cut off!")
        else:
            print("You can't go back any further.")

import random

# The Player class
class Player(object):
    def __init__(self):
        self.HP = 100
        self.hp = self.HP
        self.fists = 6
        self.feet = 5
        self.items = ["gloves"]
        self.score = 0
        self.keys = []
        
    def hit(self):
        damage = self.fists + random.randint(-self.fists //4, self.fists //4)

        if "flag" in self.items:
            damage *= 2

        return damage

    def kick(self):
        if "boots" in self.items:
            damage = self.feet + random.randint(0, self.feet)
        else:
            damage = self.feet + random.randint(-self.feet //2, self.feet //2)

        if "flag" in self.items:
            damage *= 2

        return damage

    def bitten(self, bite):
        if "scarf" in self.items:
            bite  //= 2
            
        self.hp -= bite
        print("    You got bitten for",bite,"damage, leaving you",self.hp,"health.")

    def pawed(self, paw):
        if "shirt" in self.items:
            paw  //= 2

        self.hp -= paw
        print("    You got pawed for",paw,"damage, leaving you",self.hp,"health.")
    
    def heal(self):
        self.hp = (self.hp + self.HP) //2
        
        if self.hp > 50:
            self.HP = self.hp
        else:
            self.HP = 50

    def info(self):
        facts = "Health: " + str(self.hp) + ", Score: " + str(self.score)             + ", Items: "
        jingles = "Keys: "
        attack = "Hit: "

        for item in range(len(self.items)):
            if len(self.items) == 1:
                facts = facts + self.items[item]
            elif item < len(self.items) - 1:
                facts = facts + self.items[item] + ", "
            else:
                facts = facts + "and " + self.items[item]

        for key in range(len(self.keys)):
            if len(self.keys) == 1:
                jingles = jingles + self.keys[key][:-3]
            elif item < len(self.items) - 1:
                jingles = jingles + self.keys[key][:-3] + ", "
            else:
                jingles = jingles + "and " + self.keys[key][:-3]

        if "flag" in self.items:
            attack = attack + "10 to 14, Kick: "
        else:
            attack = attack + "5 to 7, Kicks: "

        if "boots" in self.items:
            if "flag" in self.items:
                attack = attack + "10 to 20"
            else:
                attack = attack + "5 to 10"
        else:
            attack = attack + "3 to 7"
            
        print(facts)
        print(jingles)
        print(attack)

class Help(object):
    def __init__(self):
        topics = {}
        
        topics["Items"] = "Different items have different effects once picked  up. Each item's particular effect is described when you pick it up."
        topics["Health"] = "You start with 100 health that is partially  regenerates each time you move to an area."
        topics["Moving"] = "Each time you enter a room, all the routes out of  that room are listed (oriented along N-S-E-W)."
        topics["Bears"] = "Bears range in toughness from 'black' to 'grizzly'  and so on. They have a 50/50 chance of either biting or pawing. Once killed,  they remain dead. However, if you leave a room, any still-living bears will  regain their health."
        topics["Combat"] = "You have two attacks available: the punch and the  kick. The kick has more damage potential than the punch, but there's also a  chance that it won't connect properly, doing less damage, and is thus less  reliable than punches. As you collect items, your resistance to attacks and  your attacks themselves grow stronger. If you ever fear you'll lose a fight  you also have a can of bear spray that allows you to retreat a room."
        topics["Environment"] = "You can take some items from the  environment, and use those items on the environment (within certain contexts)."
        topics["Interface.Moving"] = "To move in a direction, simply  type it (e.a. 'north', 'n', and 'up' all go the same way, as do 'east', 'e', and  'right')."
        topics["Interface.Combat"] = "To attack a specific enemy, type in  an attack command ('hit','h', 'punch', or 'kick', 'k'), then leave a space and  type in the number next to the enemie's name (h 2 == punches the 2nd enemie on  the enemy list). If you just input an attack, without specifying an enemy, you  will attack the first enemy in line (which may be the only enemy in the room).  To use your spray, simply enter 'spray' (this will not work if there are no  paths)."
        topics["Interface.Environment"] = "To take an item, type in 'take'  and the item's name (listed in parenthesis) (take key == places the key in  your inventory). To use an item (unlock a door, overcome a physical obstacle),  type in 'use' and then the item you wish to use (use key == unlocks the door)"
        topics["Options"] = "There are two modes of play available: 'busy'  mode, the default, and 'clean' mode. Busy mode retains all of the text, while  clean mode constantly removes it (and also keeps you up to date on your  status). To toggle between the two, simply input 'clean'."

        self.topics = topics

    def listTopics(self):
        including = "Select any of the following: "

        for topic in self.topics:
            including = including + topic + ", "

        return including[:-2]

    def assist(self):
        print(self.listTopics() , "\nEnter 'q' to quit.")

        while True:
            topic = input("Topic: ")

            if topic in self.topics:
                print()
                print(self.topics[topic])
                print()
            elif topic == 'q':
                break
            else:
                print("Invalid topic.")

class Input(object):
    def __init__(self):
        actions = {}
        
        actions["north"] = ["north","n","up"]
        actions["south"] = ["south","s","down"]
        actions["east"] = ["east","e","right"]
        actions["west"] = ["west","w","left"]
        actions["spray"] = ["spray","bs","repell"]
        actions["look"] = ["look","l","examine","survey"]
        actions["glance"] = ["glance","g"]
        actions["quit"] = ["quit","q","end"]
        actions["help"] = ["help"]
        
        actions["hit"] = ["hit","h","punch"]
        actions["kick"] = ["kick","k","boot"]
        actions["take"] = ["take","t","grab"]
        actions["use"] = ["use","u"]
        actions["player"] = ["player","p","i","me"]

        actions["clean"] = ["clean","busy","keep","clear"]

        self.actions = actions

    def cin(self):
        actions = self.actions
        corrected = False
        
        while True:
            action = input("Your move: ")
            action = action.strip().lower().split()

            if len(action) > 0:
                for gen in actions:
                    for spec in actions[gen]:
                        if spec == action[0]:
                            # attack
                            if (gen == "hit") or (gen == "kick"):
                                try:
                                    action[1] = int(action[1]) - 1
                                except:
                                    try:
                                        action[1] = 0
                                    except:
                                        action.append(0)
                                return gen, action[1]
                            # utilize
                            elif (gen == "take") or (gen == "use"):
                                try:
                                    return gen,action[1]
                                except:
                                    try:
                                        action[1] = 0
                                    except:
                                        action.append(0)
                            # one-word that's not help
                            elif (gen == "clean") or (gen == "player") or (gen == "look") or (gen == "glance") or (gen == "spray") or (gen == "quit"):
                                return gen
                            # move
                            elif (gen == "north") or (gen == "south") or (gen == "east") or (gen == "west"):
                                return "move",gen
                            # help
                            elif gen == "help":
                                assistance = Help()
                                assistance.assist()
                                corrected = True
                                break
                            else:
                                print("What in Stephen's name does that have to do with your mission?!")
import time

class Cutscenes():
    @staticmethod
    def Intro():
        print("--Incoming transmission from Stephen Colbert...")

        for i in range(1):
            time.sleep(1)
            print("...")
            
        print("C: I have a top secret mission for you, of the utmost importance to our Nation.\nA coalition of bears has occupied French-Canadia, which was admittedly a smart\npick for invasion and occupation.")

        time.sleep(5)

        print("C: As usual, neither the French nor the Canadians have the balls to oust the\nbears, and they've been uninterrupted in their sinister plot to create a\nPolar-Grizzly hybrid, which we've dubbed the 'Prizzly Bear'.")

        time.sleep(6)

        print("C: I would be proud to take care of this myself, but a tragic croquet accident\nlast week left my wrist horribly strained such that my success could not be\nguaranteed.")

        time.sleep(6)

        print("C: Your mission, if you've got the brass, is to infiltrate the bears' HQ,\nknown only as Bearea 51, and destroy the Prizzly Bear. Secondary objectives\ninclude the rescuing of any prisoners you find, the disposal of any bears,\nand disruption of any propaganda systems.")

        time.sleep(6)

        print("C: Now, I know that it's against your instincts to help the French, but it's\nour moral duty as Christians to help those less fortunate. Think of it as\nthe Right Man's Burden.")

        time.sleep(4)

        accept = input("Do you accept this mission? ")
        accept = accept[0].lower()

        if accept == 'y':
            print("C: Good soldier.")
            time.sleep(2)
        else:
            print("C: Too bad. You're going, and that's final.")
            time.sleep(.5)

        print("C: This mission is extremely dangerous, so I am bequeaving to you my secret\nanti-bear weapons, passed down through generations of Colberts:\nThe Bearskin Gloves of Truthy Fists.")
        print("C: Use them wisely. I'll keep in contact as your mission progresses.\nAsk for help if you need any information, and Good Luck...")

        time.sleep(6)

        for i in range(2):
            time.sleep(1)
            print("...")
        time.sleep(1)
        
        print("(...2 weeks later, after enduring grave cold, hunger, and danger winding your\nway up through Canadia and tracking down Bearea 51, you emerge from a cave\nsystem, only to have it collapse behind you...)")

        time.sleep(3)

def Happy():
    print("The power of 0'Reilly compels you!")
    time.sleep(1)
    print("The Power of O'Reilly Compels You!")
    time.sleep(2)
    print("The POWER of O'REILLY COMPELS YOU!")
    time.sleep(3)
    print("(The Prizzly Bear, overwhelmed by your intense faith, falls over.)")
    time.sleep(2)
    print("C: Good job! You did it!")

    for i in range(2):
        time.sleep(2)
        print("...")
    time.sleep(2)
    
    print("C: What's he doing with his wrist?")
    time.sleep(1)
    print("(The Prizzly Bear does something with his wrist...)")
    time.sleep(1)
    print("C: Oh no, he's activated some kind of wrist-mounted bomb!")
    time.sleep(1)
    print("(... and starts a long, deep, throaty laugh)")
    time.sleep(1)
    print("C: Get out of there! He's going to explode!")

    time.sleep(1)
    print("...")
    time.sleep(2)
    
    print("(You hear an eagle's cry...)")

    for i in range(2):
        time.sleep(1)
        print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    
    print("(Stephen Jr. swoops out of the sky and lifts you away)")
    time.sleep(1)
    print("(Just then, a massive explosion rips through Bearea 51, but you   and\nStephen Jr. are a safe distance away)")
    time.sleep(2)
    print("C: *sniff* Congratulations! You did it! I couldn't be prouder if  you were my\nown son! Tip of the hat!")
    time.sleep(3)
    print("(You and Stephen Jr. fly off into the distant sunset, content in  the knowledge\nthat you've kept freedom alive to see another day...)")
import time
import random
import os

base = Level()
player = Player()
cin = Input()
gameWon = False
moved = False
clean = False
eagled = False

Cutscenes.Intro()

print(base.room.info())

print("C: Ignoring the quotations, enter 'n' to head North.\n")

while gameWon == False:
    act = cin.cin()
    # movement
    if act[0] == "move":
        result = base.move(act[1])
        if result == True:
            moved = True
            player.heal()
            print()
    # hitting
    elif act[0] == "hit":
        if len(base.room.bears) == 0:
            print("    There are no bears here.")
        elif act[1] >= len(base.room.bears):
            print("    You probably shouldn't be focusing your attention on the imaginary bears\n   instead of the real ones.")
        else:
            damage = player.hit()
            
            if base.room.num == 20:
                print("He's too powerful for mere force!")
                if not eagled:
                    player.hp = 100
                    base.room.eagle()
                    eagled = True
            else:            
                base.room.bears[act[1]].attacked(damage)
                print("    You hit",base.room.bears[act[1]].name,"for",damage,"damage, leaving it",base.room.bears[act[1]].hp,"health.")
    # kicking
    elif act[0] == "kick":
        if len(base.room.bears) == 0:
            print("    There are no bears here.")
        elif act[1] >= len(base.room.bears):
            print("    You probably shouldn't be focusing your attention on the  imaginary bears\n   instead of the real ones.")
        else:
            damage = player.kick()

            if base.room.num == 20:
                print("C: He's too powerful for mere force!")
                if not eagled:
                    player.hp = 100
                    base.room.eagle()
                    eagled = True
            else:
                base.room.bears[act[1]].attacked(damage)
                print("    You kicked",base.room.bears[act[1]].name,"for",damage," damage, leaving it",base.room.bears[act[1]].hp,"health.")
    # taking
    elif act[0] == "take":
        result = base.room.take(act[1])
        if result != None:
            if result == "captives":
                print("You rescued some prisoners!")
                player.score += 10
            elif len(result) > 2 and result[-3:] == "key":
                player.keys.append(result)
                player.score += 2
            elif result == "card":
                player.score += base.room.difficulty * 5 + 5
                player.items.append(result)
            else:
                player.items.append(result)
                player.score += 5
    # using   
    elif act[0] == "use":
        if (act[1] in player.items) or (base.room.num == 18):
            results = base.room.use(act[1])
        elif act[1] == "keys":
            results = base.room.use(player.keys)
        else:
            print("  No such thing.")
    # miscellaneous
    elif act == "player":
        print()
        player.info()
        print()
    elif act == "clean":
        clean *= -1
    elif act == "look":
        print(base.room.info())
    elif act == "glance":
        print(base.room.brief())
    elif act == "spray":
        base.retreat()
    elif act == "quit":
        print()
        print()
        print("You've quit the game.")
        break

    if clean == True:
        os.system("cls")
        player.info()
    
    if base.room.num == 20:
        if len(base.room.bears) < 1:
            gameWon = True

    if moved != True:
        for bear in base.room.bears:
            if bear.hp < 1:
                if bear.kind == "black":
                    player.score += 1
                elif bear.kind == "grizzly":
                    player.score += 2
                elif bear.kind == "polar":
                    player.score += 5
                else:
                    player.score += 25
                    if base.room.num == 19:
                        base.room.crash()
                        break
                print("    " + bear.name + " died.")
                base.room.bears.remove(bear)
                if len(base.room.bears) < 1:
                    print("    All the nearby bears are dead.")
                    print()
            elif random.random() <= 1.0/len(base.room.bears):
                result = bear.attack()

                if result[1] == "bite":
                    player.bitten(result[0])
                else:
                    player.pawed(result[0])                    
    else:
        moved = False

    if player.hp <= 0:
        print()
        print()
        print("You've run out of health.")
        break
    
if gameWon == False:
    print()
    print("A wag of the finger >:(")
else:
    Cutscenes.Happy()

if player.score >= 170:
    print("I'd compare you to Ayn Rand herself, with a score like",player.score)
elif player.score >= 135:
    print("You'd make a pretty good Carl Rove, with that",player.score,"of yours")
elif player.score >= 85:
    print("With your score of",player.score," I wouldn't rate you much higher than a bus driver")
elif player.score >= 40:
    print(player.score,"? You're looking a bit like Jon Stewart")
else:
    print("Even Bono could do better than your pitiful",player.score)
input()
