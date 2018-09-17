print("To start type \'I'M READY\' in all caps or \'QUIT\' to exit!!")
fromUser = input()
while True:
    if fromUser == "I'M READY":
        print("Let the games begin!")
    elif fromUser == "QUIT":
        print("Game Over!!")
        break
    else:
        print("TYPE I'M READY OR YOU CAN'T PLAY!!")
    fromUser = input()


# Variables
START_X = 0
START_Y = 0
MAP_X = 4
MAP_Y = 8

x = START_X
y = START_Y

# Commands
def go(direction):
    global x 
    global y 
    if direction == 'north':
        if (y + 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y += 1
            print("Went North. Good Job.")
    if direction == 'south':
        if (y - 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y -= 1
            print("Went South. Good Job.")
    if direction == 'east':
        if (x + 1) >= MAP_X:
            print("There's a wall there")
        else:
            x += 1
            print("Went East. Good Job.")
    if direction == 'west':
        if (x - 1) >= MAP_X:
            print("There's a wall there")
        else:
            x -= 1
            print("Went West. Good Job.")




    else:
        print("I don't understand which direction you're trying to go")

while True:
    # Print out all the stuff related to the room

    # Get input from the user
    fromUser = input()
    if fromUser == "quit":
        print("Game over!")
        break
    elif fromUser.split()[0] == "go":
        go(fromUser.split()[1])
    else:
        print("That didn't make any sense to me") 
