#This variable allows the game to meet the player. It gives the agent in the game a name.
x=input("Please insert your name: ")

#This function makes the loading information (which is given in the print functions below) go slower, so that it can immitate the loading proccess of a computer
import time
def print_slow(str):
    for letter in str:
        print (letter,end= "")
        time.sleep(.3)

#the following six print line functions are used as a decoration to make the game act like a realistic spy computer
print_slow("...")
print("System proccessing.")
print_slow("...")
print("Downloading files for member 10345673.")
print_slow("...")
print("Download complete.")

#introduces the actual purpose of the game
print(f"Welcome {x}.\nWarning: \nPlease make sure there is no one around you; this information is top secret. \nWe recommend you close your shades, turn off the lights, and make sure you are sitting somewhere isolated and comfortable. \nNow listen up,what you are about to hear next is your first mission. If you think you can handle this pressure, please press ENTER. \nTo scare you even more (because I am a mean person like that),I just want to let you know that the faith of this organization is in your hands. \nWe are counting on you Agent {x}, so press ENTER")

#this varible makes the code wait until the player actually presses ENTER
y= input(" ")

#The "narrator" of the game is now being presented
print("Good, I can see you are capable of following directions.\nAnyways, my name is Senior Agent Bob Marrow. As you should know, I am the world's most famous and most WANTED robber. \n I am known for stealing the most expensive and important history artifacts.\nI started this organization to teach ametuers (like you) how to become world-class spies (like muaaa). \nSince you are a new member to my NSOR society, I've decided to give you an easy task...Steal and return to me the four Emberaldjy Jems located in the Natural Historic Mueseum. Think you can manage that?")

#this decision is what starts the game. If the player picks no, s/he will not enter the game. If s/he picks yes, then they will enter the museum.
answer=input("Enter Yes or No...")
if answer == 'No':
    print("\nWell then coward, I see how it is. You will now automatically be deleted from the organization's list of members.I should have expected it, the life of a robber is not something an average perosn is capable of.\nEnjoy your robber-free life, but do remember if any news about the existence of this organization begins to spread, we WILL come to your house and INTERROGATE you. \nTrust me, it won't be pretty. \nNow where were we?Oh yes, Have a nice day!\n\n\n\n\n GAME OVER, LOSER")
elif answer == 'Yes':
    print(f"\nThat's what I like to hear! I can tell already, Agent {x}, that you have potential to be the next world-class spy! \nThe address has been faxed to you; make sure to arrive at the exact location at 10:00 pm sharp.\n Whatever you do, DO NOT bring anyone else with you, including your pets (no matter how tempting it may seem to bring your cat)!")

#this is when the supplies are introduced to the player
print("Press ENTER to continue to the museum.")
z= input(" ")
print(f"I'm impressed,{x}.I did not expect you to get this far. But don't get too cocky, you still have a long way to go to be like me.\nI prepared for you a bag full of supplies that might be useful for this mission. You can open the bag whenever you want, but remember there is only a limited amount of resoucres available for each material.\n Once any of the materials reach 0%, your mission is terminated and GAME OVER.\nI refuse to have a spy that does not know how to properly regulate his or her use of resources. Understood?\n Press ENTER to continue...")
a= input(" ")

#The supplies class includes a list of all the materials and number of each are available to the player throughout the mission
class Supplies(object):
    def __init__(self):
        self.flashlight = 100
        self.food = 100
        self.rope = 100
        self.weapons = 100
        self.nightvision = 100

    def go_down(self):
        self.flashlight -= 25
        self.food -= 10
        self.rope -= 50
        self.weapons -= 30
        self.nightvision -= 25

full_bag = Supplies()

#allows the player to actually get into the setting where they will steal the jems
print("*Transition-- inside the museum*")
print(f"\nVery well, Agent {x}. My buddies and I got you in, now you must get out on your own. Do you want to check your bag to make sure you have all the supplies you think you may need?")
response= input("Yes or No...")

if response == 'No':
    print("Oh I see, you think you are too good for that, huh? Well let me tell you something agent, this is NOT an easy job. Suit yourself I guess.\nIf you fail, don't blame it on me. Ugh, let's continue.")
elif response == 'Yes':
    print("That is what I expected from you, what a good student you are agent. Here you go:  ")
    print(full_bag)

#player decides where to start collecting the jems
first_move= input("\nSo, which room do you want to go into first? I recommend you begin in the North room as a warmup.My security man says it is the easiest room to get by. But, since it is YOUR mission, by all means please do decide for yourself. \n\nPick 'North Room' or 'East Room' or 'South Room' or 'West Room'...")

if first_move == 'North Room':
    print("I love being listened to! Trust me kid, this will get you far. TO THE NORTH ROOM YOU GO!")

    print("*Transition--- North Room*")
elif first_move == 'East Room':
    print("Ok, do it your way, but if you die or lose right at the start, I am just going to laugh... HAAA. TO THE EAST ROOM YOU GO!")

    print("*Transition--- East Room*")
elif first_move == 'South Room':
    print("Ok, do it your way, but if you die or lose right at the start, I am just going to laugh... HAAA. TO THE SOUTH ROOM YOU GO!")

    print("*Transition--- South Room*")
elif first_move == 'West Room':
    print("Ok, do it your way, but if you die or lose right at the start, I am just going to laugh... HAAA. TO THE WEST ROOM YOU GO!")

    print("*Transition--- West Room*")












