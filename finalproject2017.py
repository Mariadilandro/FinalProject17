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
print("Good, I can see you are capable of following directions.\nAnyways, my name is Senior Agent Bob Marrow. As you should know, I am the world's most famous and most WANTED robber. \n I am known for stealing the most expensive and important history artifacts.\nI started this organization to teach ametuers (like you) how to become world-class spies (like muaaa). \nSince you are a new member to my NSOR society, I've decided to give you an easy task...Steal and return to me the four Emberaldjy gems located in the Natural Historic Mueseum. Think you can manage that?")

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
print(f"I'm impressed,{x}.I did not expect you to get this far. But don't get too cocky, you still have a long way to go to be like me.\nI prepared for you a bag full of supplies that might be useful for this mission, but remember there is only a limited amount of each supply available.\n Once any of the materials reach 0, your mission is terminated and GAME OVER.\nThe resources provided are to help you not get caught. If you do, well then it's GAME OVER for you. Understood?\n Press ENTER to continue...")
a= input(" ")

#The supplies class includes a list of all the materials and number of each are available to the player throughout the mission
class Supplies(object):
    def __init__(self):
        self.flashlight = 100
        self.rope = 100
        self.chainsaw = 100
        self.nightvision = 100
        self.gemscollected = 0

    def change(self):
        self.flashlight -= 2
        self.rope -= 10
        self.chainsaw -= 100
        self.nightvision -= 1
        self.gemscollected += 25

full_bag = Supplies()

#allows the player to actually get into the setting where they will steal the gems
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the main hall of the museum*")
print(f"\nVery well, Agent {x},my buddies and I got you in, now you must get out on your own. It won't be easy, but I have faith in you. Each room has a different obstacle you must overcome,so make sure to be careful.\nThe museum is comprised of 4 exhibits: the North room, East room, South room, and West room. One gem is found in each room.\nWe will start by entering the North room. Press ENTER to continue")
b= input(" ")

#player is being told where the gems are and where they will be starting
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the North Room*")
print("\nOk, so from here you are walking on your own, but don't worry because I will be giving you hints and advice through a walkie talkie. In this room all you have to do is just walk in, grab the gem, and walk out. Easy peasy lemon squeezy! You may begin. Press ENTER to continue")
c= input(" ")

#the player is walking into the North room and given the directions as to how to grab the first gem
print("In order to walk up to the gem, you have to pick the lock.")

#the player is deciding how to pick the lock
open_lock= input("Do you want me to give you a hint as to how to open the lock, or do you want to figure it out yourself?\na. Yes help me,I AM DESPERATE PLEASE!\nb. Pffff, no way.I can do this by myself.\nOnly enter the letter: ")
if open_lock == 'a':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("What a good decision!\nFor a second I thought you were going to use a chainsaw or something to try to break it open, hahaha how stupid would that be.\nThe lock is rather easy to pick actually, all you have to do is guess the code, which luckily is only ONE number you have to input!")

    #allows the player to figure out the lock combination
    secret_number = 3
    print("--------------------------------------------------------------------------------------------------------------------")
    guess = input("\nEnter a number from 0 to 20 for the lock's code: ")
    while guess != secret_number:
        guess = int(input("Is that seriously what you chose? Try again: "))
    print("Nice job, you picked the lock!Press ENTER to grab the first gem.")
    c=input(" ")
    print("--------------------------------------------------------------------------------------------------------------------")
    full_bag.change()
    print("Percent of gems collected in the mission: ", full_bag.gemscollected)

#gives the options the player has if he/she does not want the hint
elif open_lock == 'b':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Oh so you think you're like what,a proffesional at this now? Hate to break it to you, but you aren't.")
    first_choice = input("So, what are you going to do then to pick the lock?\na. Umm... obviously use the chainsaw from my bag\nb. I'll just give up(if you do this, then you will lose the game)\nc. I'm starting to think actually that asking for a hint is a good idea\nEnter only the letter: ")
    if first_choice == 'a':
        full_bag.change()
        print("--------------------------------------------------------------------------------------------------------------------")
        print("What a stupid decision.")
        print("Percent of weaponry aka chainsaw source left to use in the mission: ", full_bag.chainsaw)
        print("Well, looks like you got to 0% quickly. Sorry but you know what that means....\n\n\n\n\n\nGAME OVER")
    elif first_choice == 'b':
        print("--------------------------------------------------------------------------------------------------------------------")
        print("So I guess for once my gut feeling was wrong about you. I thought you would be a great spy but never mind, you suck!\nYou can't even figure out how to pick a lock, guess that means:\n\n\n\n\n\nGAME OVER")
    elif first_choice == 'c':
        print("--------------------------------------------------------------------------------------------------------------------")
        print("What a good decision!\nIt is rather simple to pick actually, all you have to do is guess the code, which is only ONE number you have to input!")
        secret_number = 3
        guess = int(input("\nEnter a number from 0 to 20 for the lock's code: "))
        while guess != secret_number:
            guess = input("Is that seriously what you chose? Try again: ")
        print("Nice job, you picked the lock! The door is opening for you and the first gem is right in there. Press ENTER to grab the gem.")
        d=input(" ")
        print("--------------------------------------------------------------------------------------------------------------------")

        #gives the percent completion of the game basically
        full_bag.change()
        print("Percent of gems collected in the mission: ", full_bag.gemscollected)


#the class below gives the generic details of the East, South, and West rooms
class Room(object):
    """Room object defines an exhibit in the museum"""
    def __init__(self,description,riddle,supplies):
        self.description= description
        self.riddle= riddle
        self.supplies= supplies

#gives the definition of each room using the classroom
East_room = Room("The North room was a warm up, now the hard part begins. This room has invisible lasers which if you step on will be GAME OVER.","What are the four houses at Hogwarts School of Witchcraft and Wizardry?","Nightvision goggles")
South_room = Room("If you thought the East room was hard, well this room is much worse. This room has a security gaurd protecting the gem. Fortunetly he fell asleep on the job (which is honestly something I would do too hahaha). You just have to make sure not to wake him up by stepping on creeky tiles.","How many chambers are there in a dog's heart?","Rope")
West_room = Room("Wow, I am truly impressed. This is a hard mission and look at you agent, you are at the end of this journey. Now, some say this is the most difficul room to complete. This is the storage room, which is soon to be another exhibit. It contains all the artifacts that will be used once the new exhibit is constructed, including the last gem.  You have to make sure not to knock any of the artifacts over in the dark.","What did the famous Hollywood sign, located in Los Angeles, originally say?","flashlight")

#the player is now being transferred into the second room of the museum
print("--------------------------------------------------------------------------------------------------------------------")
print("See, that wasn't so bad. Now, we have to head to the East room. Press ENTER to continue...")
e=input(" ")
print("*Inside the East room*")
print(East_room.description)
f=input("Press enter to continue...")
print("--------------------------------------------------------------------------------------------------------------------")

#the player has to figure out how to get through the lasers
first_supply= input("Do you want to use a supply from the bag to make sure you don't step on a laser?\na.Yes\nb.No\nEnter the letter: ")
if first_supply == 'a':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("I would have chosen the same thing. The perfect supply to use in this type of situation are the ",East_room.supplies)
    print("The gem is 13 steps away, so lets hope you have enough nightgoggle energy to get you there without the energy going down to 0%. Press ENTER to continue...")
    g= input(" ")
    print("--------------------------------------------------------------------------------------------------------------------")
    for o in range(13):
        full_bag.change()
        print("Amount of night vision left:", full_bag.nightvision)
    print("You made it to the gem safe and sound without starting the alarm, CONGRATULATIONS! But, that is not the only thing you have to worry about. In order to grab ahold of the gem, you have to solve a trivia quesition.")
    print("--------------------------------------------------------------------------------------------------------------------")
    print(East_room.riddle)
    trivia_one= input("\nIs it: a. Thunderbird, Horned Serpent,Puckwudgie,and Wampus\nb. Ravenclaw,Horned Serpent,Puckwudgie,and Wampus\nc. Gryffindor,Ravenclaw,Hufflepuff,and Slytherin\nEnter only the letter: ")
    response_one= 'c'
    while trivia_one != response_one:
        trivia_one = input("Do you live under a rock! Try it again: ")
    print("Nice job! You solved the riddle, and now you have the second gem! Press ENTER to grab the gem.")
    h=input(" ")
    full_bag.change()
    print("Percent of gems collected in the mission: ", full_bag.gemscollected)

#the second decision the player has to get through the lasers
elif first_supply == 'b':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Wow, you are one risky spy, but hey I respect that. I guess that means you will be guessing where the lasers are located.")
    print("In order to get through the room without stepping on a laser, you have to guess the correct secret number three times in a row. If you don't, well...GAME OVER for you.")
    guess_one = input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
    if guess != secret_number:
        print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

    elif guess == secret_number:
        print("I don't know wether that was luck or you just being a pure genious, but here comes round two: ")
        secret_number2= 5
        guess_two =  input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
        if guess_two != secret_number2:
            print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

        elif guess_two == secret_number2:
            print("I don't know wether that was luck or you just being a pure genious, but here comes round three: ")
            secret_number3 = 1
            guess_three = input("\nEnter a number from 0 to 5 for your guess on the secret number: ")
            if guess_three != secret_number3:
                print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

            elif guess_three == secret_number3:
                print("I undersetimated your abilities. I always assume you will die but you keep proving me wrong. Keep up the good work.Press ENTER to grab the second gem.")
        i=input(" ")
        full_bag.change()
        print("Percent of gems collected in the mission: ", full_bag.gemscollected)

#Transition for the player to enter the South room
print("--------------------------------------------------------------------------------------------------------------------")
print("See, that wasn't so bad. Now, we have to head to the South room. Press ENTER to continue...")
j=input(" ")
print("*Inside the South room*")
print(South_room.description)
k=input("Press enter to continue...")
print("--------------------------------------------------------------------------------------------------------------------")

#the player has to figure out how to not wake up the security gaurd that is sleeping in the room
second_supply= input("Do you want to use a supply from the bag to make sure you don't step on the loud floor and end up waking the security gaurd?\na.Yes\nb.No\nEnter the letter: ")
if second_supply == 'a':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("I would have chosen the same thing. The perfect supply to use in this type of situation is the ",South_room.supplies,"This is because there is a pully right at the center of the room which will allow you to hang the", South_room.supplies,"and swing you from one end of the room to the other.Genious idea right? Muaaaa,aka me, came up with it.")
    print("The gem is only 8 steps away, so lets hope you have enough rope energy to get you there without the energy making it to 0%. Press ENTER to continue...")
    print("--------------------------------------------------------------------------------------------------------------------")
    l= input(" ")
    for o in range(8):
        full_bag.change()
        print("Amount of rope left:", full_bag.rope)
    print("You made it to the gem safe and sound without waking the security gaurd, CONGRATULATIONS! But, that is not the only thing you have to worry about. In order to grab ahold of the third gem, you have to solve yet another trivia quesition.")
    print("--------------------------------------------------------------------------------------------------------------------")
    print(South_room.riddle)
    trivia_two= input("\nIs it: a. twelve\nb. four\nc. two\nEnter only the letter: ")
    response_two= 'b'
    while trivia_two != response_two:
        trivia_two = input("Do you live under a rock! Try it again: ")
    print("Nice job! You solved the riddle, and now you have the third gem! Press ENTER to grab the gem.")
    m=input(" ")

    #gives how much of the missoin the player has completed
    full_bag.change()
    print("Percent of gems collected in the mission: ", full_bag.gemscollected)

#the other decision the player has if he does not want to use a supply
elif second_supply == 'b':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Wow, you are one risky spy, but hey I respect that. I guess that means you will be on the edge of meeting an awake gaurd.")
    print("In order to get through the room without making a noise, you have to guess the correct secret number three times in a row. If you don't, well...GAME OVER for you.")
    secret_number4 = 8
    guess_four = input("\nEnter a number from 5 to 10 for your guess on the secret number: ")
    if guess_four != secret_number4:
        print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

    elif guess_four == secret_number4:
        print("I don't know whether that was luck or you just being a pure genious, but here comes round two: ")
        secret_number5 = 10
        guess_five =  input("\nEnter a number from 5 to 10 for your guess on the secret number: ")
        if guess_five != secret_number5:
            print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

        elif guess_five == secret_number5:
            print("I don't know wether that was luck or you just being a pure genious, but here comes round three: ")
            secret_number6 = 7
            guess_six = input("\nEnter a number from 5 to 10 for your guess on the secret number: ")
            if guess_six != secret_number6:
                print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

            elif guess_six == secret_number6:
                print("I undersetimated your abilities. I always assume you will die but, you keep proving me wrong everytime. Keep up the good work.Press ENTER to grab the third gem.")
        n=input(" ")

        #shows how much of the mission the player has completed
        full_bag.change()
        print("Percent of gems collected in the mission: ", full_bag.gemscollected)


#Transition for the player to enter the West room
print("--------------------------------------------------------------------------------------------------------------------")
print("See, that wasn't so bad. Now, we have to head into the last room....the West room. Press ENTER to continue...")
p=input(" ")
print("--------------------------------------------------------------------------------------------------------------------")
print("*Inside the West room*")
print(West_room.description)
q=input("Press enter to continue...")

#the player has to figure out how to get through the room without dropping any artifacts
third_supply= input("Do you want to use a supply from the bag to make sure you don't topple over an ancient artifacst in the dark?\na.Yes\nb.No\nEnter the letter: ")
if third_supply == 'a':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("I would have chosen the same thing. The perfect supply to use in this type of situation is the ",West_room.supplies,"It illuminates the path you are taking so you can see which direction you are heading in.")
    print("The gem is really far, 40 steps to be precise.Let's hope you have enough flashlight energy to get you there before the energy gets to 0%. Press ENTER to continue...")
    r= input(" ")
    for o in range(9):
        full_bag.change()
        print("Amount of flashlgiht left:", full_bag.flashlight)
    print("You made it to the gem safe and sound without breaking any artifacts, CONGRATULATIONS! But, that is not the only thing you have to worry about. In order to grab ahold of the fourth gem, you have to solve yet another trivia quesition.")
    print("--------------------------------------------------------------------------------------------------------------------")
    print(West_room.riddle)
    trivia_three= input("\nIs it: a. Disneyland\nb. Hollywoodland\nc. Los Angeles Hollywood\nEnter only the letter: ")
    response_three= 'b'
    while trivia_three != response_three:
        trivia_three = input("Do you live under a rock! Try it again: ")
    print("Nice job! You solved the riddle, and now you have the fourth gem! Press ENTER to grab the gem.")
    s=input(" ")

    #gives the percent of the mission completed by the player
    full_bag.change()
    print("Percent of gems collected in the mission: ", full_bag.gemscollected)

#allows the player to chose then how to pass the room without using a supply from the bag
elif third_supply == 'b':
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Wow, you are one risky spy, but hey I respect that. I guess that means you will be having to feel your way forward and through the dark.")
    print("In order to get through the room without breaking anything, you have to guess the correct secret number three times in a row. If you don't, well...GAME OVER for you.")
    secret_number7 = 14
    guess_seven = input("\nEnter a number from 10 to 15 for your guess on the secret number: ")
    if guess_seven != secret_number7:
        print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

    elif guess_seven == secret_number7:
        print("I don't know wether that was luck or you just being a pure genious, but here comes round two: ")
        secret_number8= 13
        guess_eight =  input("\nEnter a number from 10 to 15 for your guess on the secret number: ")
        if guess_eight != secret_number8:
            print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")

        elif guess_eight == secret_number8:
            print("I don't know wether that was luck or you just being a pure genious, but here comes round three: ")
            secret_number9 = 11
            guess_nine = input("\nEnter a number from 10 to 15 for your guess on the secret number: ")
            if guess_nine != secret_number9:
                print(f"I guess you were a bit too risky for the first mission. I'm sorry agent {x}, but you know what this means...\n\n\n\n\n\nGAME OVER")
            elif guess_nine == secret_number9:
                print("I undersetimated your abilities. I always assume you will die but, you keep proving me wrong. And this time, it was the last gem of the mission! Press ENTER to grab the fourth gem.")
            t=input(" ")

            #shows the percent of how much of the mission the player has completed
            full_bag.change()
            print("Percent of gems collected in the mission: ", full_bag.gemscollected)


































