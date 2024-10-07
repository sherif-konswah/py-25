# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 3:29:48 TO 3:38:28
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Rock Paper Scissor -v 3

print('---------------------------------------------')
print("------------ updated RPC Game--------------")
import sys
import random
from enum  import Enum

def play_rps():
    
    class RPS(Enum):
        ROCK =1
        PAPER =2
        SCISSOR =3


    print('************************************')
    rpc1 =int(input("Player 1 : Pick Your Type...\n 1 For Rock, \n 2 For Paper, \n 3 For Scissor:\n\n"))
    rpc2 =int(random.choice("123"))

    if(int(rpc1) not in [1,2,3]):
        print("😱😱 You Must Enter Number From 1 To 3 Only!!!!")
        return play_rps()
    
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

    print("\n Play Again??")
    while True:
        playagain = input("\n Y >>> For Yes \n OR \n N >>> For Quit\n")
        if playagain.lower() not in ["y","n"]:
            continue
        else:
            break
    if playagain.lower()=="y":
        return play_rps()
    else:
        print("T🎉🎉🎉🎉🎉🎉 hank You For Playing Our Game!!!!🎉🎉🎉🎉🎉")
        sys.exit("Bye! 👋👋👋👋👋")
        

play_rps()



