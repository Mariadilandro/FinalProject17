x=input("Please insert your name: ")

import time
def print_slow(str):
    for letter in str:
        print (letter,end= "")
        time.sleep(.3)

print_slow("...")
print("System proccessing.")
print_slow("...")
print("Downloading files for member 10345673.")
print_slow("...")
print("Download complete.")

print(f"Welcome {x}. Please make sure there is no one around you; this information is top secret. \nClose your shades, turn off the lights, and make sure you are sitting somewhere isolated and comfortable. \nWhat you are about to hear is your next mission. We are counting on you Agent {x};the faith of this organization is in your hands.\n If you think you can handle this pressure, press ENTER to continue.")

y= input(" ")
print("My name is Senior Agent Bob Marrow. As you should know, I am the world's most famous and most WANTED artifact robber. I started this organization to teach ametuers how to become world-class spies. Since you are a new member, I've decided to give you an easy task...Steal the three Emberaldjy Jems from the Natural Historic Mueseum. Think you can manage it?.")

answer=input("Enter Yes or No...")
if answer == 'No':
    print("Well then, please exit this screen and log out. You will automatically be deleted from the organization's list of members. Enjoy your robber-free life, but do remember if any notice about the existence of this organization is being spread around, we WILL come to your house and INTERROGATE you. It won't be pretty. Now where were we?... Oh yes, Have a nice day!")
elif answer == 'Yes':
    print(f"That's what I like to hear. I can tell already Agent{x} that you have potential to be the next world-class spy!")








