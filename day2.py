#Course Name 
#Python full course for beginners | complete all-in-one tutorial | 9 hours
#Chanel
#Dave Gray
#From 1:20:00 in vedio
#Up To 1:42:15


import sys
import random
from enum  import Enum

class RPS(Enum):
    ROCK =1
    PAPER =2
    SCISSOR =3

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

