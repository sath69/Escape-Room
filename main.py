import access_data as ad

health = int(ad.readData("health"))

locked_rooms=['2','3']
rooms=[str(x+1) for x in range(3)]


print("\nWelcome to Escape Room Beta!!\n")
start_game=input("Start Map? (y/n): ").lower()=='y'
while True:
    if start_game:
        print("Please choose a room from 1, 2 and 3")
        room_choice=input("Chosen room: ")
        if room_choice in locked_rooms:
            print("Locked. Please complete previous level to unlock.")
        elif room_choice in rooms:
            try:
                with open(f"rooms\\room{room_choice}.py") as f:
                    exec(f.read())
            except Exception as e:
                print(e)
            else:
                if rooms.index(room_choice)!=-1:
                    try:
                        locked_rooms.remove(str(int(room_choice)+1))
                    except:
                        pass
        else:
            print("Room not Found!")
    else:
        print("Goodbye!!")
        health = 100
        ad.writeData("health",health)
        exit()

