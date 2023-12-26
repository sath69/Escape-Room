#ROOM 1
import random
import json
import sys
sys.path.append('../Projekt')
import access_data as ad

#ah weird cuz it says the health is None
health = 100
print(f"Health: {health}")

#generate a 4 Digit PIN code
PIN = f"{random.randint(0,9999):04d}"
while True:
    print("\nGAME MENU:\n")
    print("1. Open exit door")
    print("2. Open safe")
    print("3. Open desk drawer")
    print("4. Look around")

    ch1 = input("\nChoose any of the options (1,2,3,4): ")
    
    if ch1 == "1":
        if not found_key:
            print("I need a key to unlock it!")
        else:
            print("Unlocked the door!")
            print("Escaped Room Successfully!!!")
            break

    elif ch1 == "2":
        if found_pin and not found_key:
            user_PIN = input("Please enter the PIN: ")

            if user_PIN == PIN:
                print("Unlocked Safe. Received a key.")
                found_key = True
            else:
                print("Invalid PIN!!!")
                
        elif found_key:
            print("Safe is already unlocked.")
        else:
            print("I don't know the code!")

    elif ch1 == "3":
        if found_desk_key and not found_pin:
            print(f"Found a piece of card with a 4-digit number on it. The number is {PIN}.")
            found_pin = True
        elif found_desk_key:
            print("The desk is already unlocked.")
        else:
            print("Looks like the desk is locked.")

    elif ch1=='4':
        if not found_desk_key:
            print("Found a desk key.")
            found_desk_key = True
        else:
            print("Nothing useful here.")

    else:
        print("Invalid option!!!")
