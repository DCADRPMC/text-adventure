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
