# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 2:43:07 To 3:05:51
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#LOOPS
print('***While Loop***')
value = 1

while value < 10:
    print(value)
    value+=1

print('-------------------')
#brak loop
value = 0
while value <= 11:
    print(value)
    value+=1
    if value ==7:
        continue
    
    # if   value == 5:
    #     break
    
else:
    print('Value now equal '+str(value))

    



print('------------------------------------------------------')
print('***For Loop***')

names=['Ahmed','Ali','Alaa','Adam']
for x in names:
    print(x)



for x in "فاسقيناكموه":
    print(x)

for x in names:
    if x == "Alaa":
        break
    print(x)

print('-------')
for x in names:
    if x == "Alaa":
        continue
    print(x)

print('-------Range Loop----')
for x in range(6):
    print(x)
print('-------')

for x in range(2,5):
    print(x)

print('-------')
# increment more one 
for x in range(0,101,10):
    print(x)
else:
    print('Glad , We Done')

print('-------')
actions=["coders","doctor","accountant"]

for name in names:
    for action in actions:
        print(name + " is " + action +".")
print('-------')


for action in actions:
    for name in names:
        print(name + " is " + action +".")


print('---------------------------------------------')
print("------------ updated RPC Game--------------")
import sys
import random
from enum  import Enum

class RPS(Enum):
    ROCK =1
    PAPER =2
    SCISSOR =3

playagain = True
while playagain:
    print('****************************************')

    #user input

    # value = input('Please  enter a value : \n')

    # print("Welcome Mr." + value)


    rpc1 =int(input("Player 1 : Pick Your Type...\n 1 For Rock, \n 2 For Paper, \n 3 For Scissor:\n\n"))
    rpc2 =int(random.choice("123"))


    print("You Chose " + str(RPS(rpc1)).replace("RPS.","")  + ".")




    print("Computer Chose " + str(RPS(rpc2)).replace("RPS.","") + ".")


    if rpc1 == rpc2 :
        print("☹️ It\'s A Tie")
    elif rpc1 == 1 and rpc2 == 2 :
        print("🐍 Computer Win >>>> Paper win Rock")
    elif rpc1 == 2 and rpc2 == 1 :
        print("🎉 You Win >>>> Paper win Rock")
    elif rpc1 == 3 and rpc2 == 2 :
        print("🎉 You Win >>>> Scissor win Paper")
    elif rpc1 == 2 and rpc2 == 3 :
        print("🐍 Computer Win >>>> Scissor win Paper")
    elif rpc1 == 3 and rpc2 == 1 :
        print("🐍 Computer Win >>>> Rock Win Scissor")
    else: # rpc1 == 1 & rpc2 == 3 :
        print("🎉 You Win >>>> Rock Win Scissor")

    playagain = input("\n Play Again ??? \n Y >>> For Yes \n OR \n Q >>> For Quit \n\n")

    if playagain.lower()=="y":
        continue
    else:
        print("T🎉🎉🎉🎉🎉🎉 hank You For Playing Our Game!!!!🎉🎉🎉🎉🎉")
        print("Bye")
        playagain = False
    

