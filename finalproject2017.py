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

print("--------------------------------------------------------------------------------------------------------------------")
#introduces the actual purpose of the game
print(f"Welcome {x}.\nWarning: \nPlease make sure there is no one around you; this information is top secret. \nWe recommend you close your shades, turn off the lights, and make sure you are sitting somewhere isolated and comfortable. \nNow listen up,what you are about to hear next is your first mission. If you think you can handle this pressure, please press ENTER. \nTo scare you even more (because I am a mean person like that),I just want to let you know that the faith of this organization is in your hands. \nWe are counting on you Agent {x}, so press ENTER")
#this varible makes the code wait until the player actually presses ENTER
y= input(" ")

print("--------------------------------------------------------------------------------------------------------------------")
#The "narrator" of the game is now being presented
print("Good, I can see you are capable of following directions.\nAnyways, my name is Senior Agent Bob Marrow. As you should know, I am the world's most famous and most WANTED robber. \n I am known for stealing the most expensive and important history artifacts.\nI started this organization to teach ametuers (like you) how to become world-class spies (like muaaa). \nSince you are a new member to my NSOR society, I've decided to give you an easy task...Steal and return to me the four Emberaldjy Jems located in the Natural Historic Mueseum. Think you can manage that?")

#this decision is what starts the game. If the player picks no, s/he will not enter the game. If s/he picks yes, then they will enter the museum.
answer=input("Enter yes or no...")
if answer == 'no':
    print("\nWell then coward, I see how it is. You will now automatically be deleted from the organization's list of members.I should have expected it, the life of a robber is not something an average perosn is capable of.\nEnjoy your robber-free life, but do remember if any news about the existence of this organization begins to spread, we WILL come to your house and INTERROGATE you. \nTrust me, it won't be pretty. \nNow where were we? Oh yes, Have a nice day!\n\n\n\n\n GAME OVER, LOSER")
elif answer == 'yes':
    print(f"\nThat's what I like to hear! I can tell already, Agent {x}, that you have potential to be the next world-class spy! \nThe address has been faxed to you; make sure to arrive at the exact location at 10:00 pm sharp.\n Whatever you do, DO NOT bring anyone else with you, including your pets (no matter how tempting it may seem to bring your cat)!")

#this is when the supplies are introduced to the player
print("Press ENTER to continue to the museum.")
z= input(" ")

print("--------------------------------------------------------------------------------------------------------------------")
print(f"I'm impressed,{x}.I did not expect you to get this far. But don't get too cocky, you still have a long way to go to be like me.\nI prepared for you a bag full of supplies that might be useful for this mission, but remember there is only a limited amount of each available supply.\n Once any of the materials reach 0, your mission is terminated and GAME OVER.\nThe resources provided are to help you not get caught. If you do, well then it's GAME OVER for you. Understood?\n Press ENTER to continue...")
a= input(" ")

#The supplies class includes a list of all the materials and number of each are available to the player throughout the mission
class Supplies(object):
    def __init__(self):
        self.flashlight = 100
        self.chainsaw = 100
        self.nightvision = 100
        self.jemscollected = 0

    def change(self):
        self.flashlight -= 25
        self.chainsaw -= 100
        self.nightvision -= 5
        self.jemscollected += 25

full_bag = Supplies()

#allows the player to actually get into the setting where they will steal the jems
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the main hall of the museum*")
print(f"\nVery well, Agent {x},my buddies and I got you in, now you must get out on your own. It won't be easy, but I have faith in you. Each room has a different obstacle you must overcome, like security gaurds, so make sure to be careful.\nThe museum is comprised of 4 exhibits: the North room, East room, South room, and West room. One jem is found in each room.\nWe will start by entering the North room. Press ENTER to continue")
b= input(" ")
#player is being told where the jems are and where they will be starting
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the North Room*")
print("\nOk, so from here you are walking on your own, but don't worry because I will be giving you hints and advice through a walkie talkie. In this room all you have to do is just walk in, grab the jem, and walk out. Easy peasy lemon squeezy! You may begin. Press ENTER to continue")
c= input(" ")
print("--------------------------------------------------------------------------------------------------------------------")

#the player is walking into the North room and given the directions as to how to grab the first jem
print("In order to walk up to the jem, you have to open the lock.")
print("--------------------------------------------------------------------------------------------------------------------")
open_lock= input("Do you want me to give you a hint as to how to open the lock, or do you want to figure it out yourself?\nA.Yes help me, I AM DESPERATE AND NEED YOU, THE AMAZING AND HANDSOME GOD OF ROBBERS, TO HELP ME!\nB.Pffff, no way.I can do this by myself, I am too good.\nOnly enter the capital letter: ")
if open_lock == 'A':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("What a good decision!\nFor a second I thought you were going to use a chainsaw or something to try to break it open, hahaha how stupid would that be.\nThe lock is rathe reasy to pick actually, all you have to do is guess the code, which luckily is only ONE number you have to input!")

    #allows the player to figure out the lock combination
    secret_number = 3
    print("--------------------------------------------------------------------------------------------------------------------")
    guess = input("\nEnter a number from 0 to 20 for the lock's code: ")
    while guess != secret_number:
        guess = int(input("Is that seriously what you chose? Try again: "))
    print("Nice job, you picked the lock!Press ENTER to grab the first jem.")
    c=input(" ")
    print("--------------------------------------------------------------------------------------------------------------------")
    full_bag.change()
    print("Percent of jems collected in the mission: ", full_bag.jemscollected)

#gives the options the player has if he/she does not want the hint
elif open_lock == 'B':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Oh so you think you're like what,a proffesional at this now? Hate to break it to you, but you aren't.")
    first_choice = input("So, what are you going to do then to pick the lock?\na. Umm... obviously use the chainsaw from my bag\nb. I'll just give up(just saying that if you do this, then you will die and lose the game)\nc. I'm starting to think actually that asking for a hint is a good idea\nEnter only the lowercase letter: ")
    if first_choice == 'a':
        full_bag.change()
        print("--------------------------------------------------------------------------------------------------------------------")
        print("What a stupid decision.")
        print("Percent of weaponry aka chainsaw source left to use in the mission: ", full_bag.chainsaw)
        print("Well, looks like you got to 0% quickly. Sorry but you know what that means....\n\n\n\n\n\nGAME OVER")
    elif first_choice == 'b':
        print("--------------------------------------------------------------------------------------------------------------------")
        print("So I guess for once my gut feeling was wrong. I thought you would be a great spy but never mind, you suck!\nYou can't even figure out how to pick a lock, guess that means:\n\n\n\n\n\nGAME OVER")
    elif first_choice == 'c':
        print("--------------------------------------------------------------------------------------------------------------------")
        print("What a good decision!\nFor a second I thought you were going to use a chainsaw or something to try to break it open, hahaha how stupid would that be.\nIt is rather simple to solve actually, all you have to do is guess the code, which is only ONE number you have to input!")
        secret_number = 3
        guess = int(input("\nEnter a number from 0 to 20 for the lock's code: "))
        while guess != secret_number:
            guess = input("Is that seriously what you chose? Try again: ")
        print("Nice job, you opened the lock! The door is opening for you and the first jem is right in there. Press ENTER to grab the jem.")
        d=input(" ")
        print("--------------------------------------------------------------------------------------------------------------------")
        full_bag.change()
        print("Percent of jems collected in the mission: ", full_bag.jemscollected)


#the class below gives the generic details of the East, South, and West rooms
class Room(object):
    """Room object defines an exhibit in the museum"""
    def __init__(self,description,riddle,supplies):
        self.description= description
        self.riddle= riddle
        self.supplies= supplies

East_room = Room("The North room was a warm up, now the hard part begins. This room has invisible lasers that if you step on, the alarm goes off and GAME OVER.","What are the four houses at Hogwarts School of Witchcraft and Wizardry?","Nightvision goggles")
South_room = Room("If you thought the East room was hard, well this room is much worse. This room has a security gaurd protecting the jem. Fortunetly he fell asleep on the job (which is honestly something I would do too hahaha). You just have to make sure not to wake him up by stepping on such creeky tiles.","How many chambers are there in a dog's heart?","Rope")
West_room = Room("Wow, I am truly impressed. This is a hard mission and look at you agent, you are at the end of this journey. Some may say this is the most difficul room to get through. This is the storage room, which is soon to become another exhibit. It contains all the artifacts that will be found once the exhibit is constructed, inclusing the last jem.  You have to make sure not to knock any of the artifacts over in the dark.","What did the famous Hollywood sign, located in Los Angeles, originally say?","flashlight")

#the player is now being transferred into the second room of the museum
print("--------------------------------------------------------------------------------------------------------------------")
print("See, that wasn't so bad. Now, we have to head to the East room. Press ENTER to continue...")
e=input(" ")
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the East room*")
print(East_room.description)
f=input("Press enter to continue...")
print("--------------------------------------------------------------------------------------------------------------------")

#the player has to figure out how to get through the lasers
first_supply= input("Do you want to use a supply from the bag to make sure you don't step on a laser?\na.Yes\nb.No\nEnter the lowercase letter: ")
if first_supply == 'a':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("I would have chosen the same thing. The perfect supply to use in this type of situation are the ",East_room.supplies)
    print("The jem is 20 steps away, so lets hope you have enough nightgoggle energy to get you there without the energy making it to 0%. Press ENTER to continue...")
    print("--------------------------------------------------------------------------------------------------------------------")
    g= input(" ")
    for o in range(21):
        full_bag.change()
        print("Amount of night vision left:", full_bag.nightvision)
    print("--------------------------------------------------------------------------------------------------------------------")
    print("You made it to the jem safe and sound without starting the alarm, CONGRATULATIONS! But, that is not the only thing you have to worry about. In order to grab ahold of the jem, you have to solve a trivia quesition.")
    print("--------------------------------------------------------------------------------------------------------------------")
    trivia_one= input(East_room.riddle,"\nIs it: a. Thunderbird, Horned Serpent,Puckwudgie,and Wampus\nb. Ravenclaw,Horned Serpent,Puckwudgie,and Wampus\nc. Gryffindor,Ravenclaw,Hufflepuff,and Slytherin\nEnter only the lowercase letter: ")
    response_one= 'c'
    while trivia_one != response_one:
        print("Do you live under a rock! Try it again: ")
    print("Nice job! You solved the riddle, and now you have the second jem! Press ENTER to grab the jem.")
    h=input(" ")
    print("--------------------------------------------------------------------------------------------------------------------")
    full_bag.change()
    print("Percent of jems collected in the mission: ", full_bag.jemscollected)

elif first_supply == 'b':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Wow, you are one risky spy, but hey I respect that. I guess that means you will be guessing where the lasers are located.")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("In order to get through the room without stepping on a laser, you have to guess the correct secret number three times in a row. If you don't, well...GAME OVER for you.")
    guess_one = input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
    if guess != secret_number:
        print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")
    elif guess == secret_number:
        print("I don't know wether that was luck or you just being a pure genious, but here comes round two.Enter a number from 0 to 5 for your guess on the secret number: ")
        secret_number2= 5
        guess_two =  input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
        if guess_two != secret_number2:
            print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")
        elif guess_two == secret_number2:
            print("I don't know wether that was luck or you just being a pure genious, but here comes round two.Enter a number from 0 to 5 for your guess on the secret number: ")
            secret_number3 = 1
            guess_three = input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
            if guess_three != secret_number3:
                print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")
            elif guess_three == secret_number3:
                print("I undersetimated your abilities. I always assume you will die but, you keep proving me wrong everytime. Keep up the good work.Press ENTER to grab the jem.")
        i=input(" ")
        print("--------------------------------------------------------------------------------------------------------------------")
        full_bag.change()
        print("Percent of jems collected in the mission: ", full_bag.jemscollected)

print("--------------------------------------------------------------------------------------------------------------------")
print("See, that wasn't so bad. Now, we have to head to the South room. Press ENTER to continue...")
j=input(" ")
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the South room*")


































