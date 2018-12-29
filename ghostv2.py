import random
def ghostgame(room, ghost, c):
    i = 0
    count = 0
    while (True):
        print("count =", count)
        choice = int(input("Enter room "))

        if (choice > room):
            print("You don't have enough rooms")
            break

        if (choice != c[i]):
            print("Room is free, come in")
            count = count + 1
        else:
            print("GAME OVER")
            print("Your count = ", count)
            break



while (True):
    room = int(input("How many rooms?"))
    ghost = int(input("How many ghosts?"))

    if (ghost > room):
        print("ghosts more than rooms, you will die anyway")
        break

    # to fix bag with last room
    roomplusone = room + 1
    # to fix bag with last room

    c = random.sample(range(1, roomplusone), ghost)

    ghostgame(room, ghost, c)



