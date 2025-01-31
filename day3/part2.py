def treasureisland():
    #treasure island game 
    choice_1 = input("welcome to the treasure island game\n you are at crossroads which direction would you like to go \"right\" or \"left\"\n").lower().strip()
    #gamelogic
    if choice_1 != "left":
        print("game over")
        return
    choice_2 = input("swim or wait\n")
    if choice_2 != "wait":
        print("you have been mauled")
        return
    choice_3 = input("which door would you like to enter to win the prize\n")
    if choice_3 != "blue":
        print("you have lost return")
    else:
        print("you are the winner of the game")
        return

treasureisland()
