# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 3:57:16 To 4:16:17
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("********* Closure *********")
# Note ::: Closure is a function have access to scope of its parent
# function   after the parent function has returned

def parent_function(person,coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if(coins > 1):
            print("\n "+person + " has "+ str(coins) +" coins lest.")
        elif (coins ==1):
            print("\n "+person + " has "+ str(coins) +" coin lest.")
        else:
            print("\n "+person + " is out of coins")
    return play_game


tommy = parent_function("Tommy",3)
jenny = parent_function("jenny",6)
tommy()
tommy()
jenny()
tommy()

jenny()
jenny()
jenny()


# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
