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


def rps():
        
    game_count = 0
    com_wins_count = 0
    player_wins_count = 0


    def play_rps():
        nonlocal game_count
        nonlocal com_wins_count
        nonlocal player_wins_count

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
        
        print(f"You Chose {str(RPS(rpc1)).replace("RPS.","")}  .")
        print(f"Computer Chose {str(RPS(rpc2)).replace("RPS.","")}.")
        

        def decide_winner (rpc1,rpc2):
            nonlocal player_wins_count
            nonlocal com_wins_count

            if rpc1 == rpc2 :
                return"☹️ It\'s A Tie"
            elif rpc1 == 1 and rpc2 == 2 :
                com_wins_count += 1
                return"🐍 Computer Win >>>> Paper win Rock", com_wins_count
            elif rpc1 == 2 and rpc2 == 3 :
                com_wins_count += 1
                return"🐍 Computer Win >>>> Scissor win Paper" ,com_wins_count
            elif rpc1 == 3 and rpc2 == 1 :
                com_wins_count +=1
                return"🐍 Computer Win >>>> Rock Win Scissor" , com_wins_count
                
            else:
                player_wins_count +=1
                return"🎉 You Win >>>> Rock Win Scissor" , player_wins_count

        game_result = decide_winner(rpc1,rpc2)
        print(game_result)
        game_count
        game_count +=1

        print(f"\n Game Count : {str(game_count)} \n Total Result  : \n Player  >>>   {str(player_wins_count)}    VS    {str(com_wins_count)}    <<<   Com")

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
            print(" Thank You For Playing Our Game!!!")
            if(player_wins_count == com_wins_count ):
                print ("Final result is Tie")
            elif(player_wins_count > com_wins_count):
                print("T🎉🎉🎉🎉🎉🎉 Gongratulation , You Are the Winner T🎉🎉🎉🎉🎉🎉")
            else:
                print("🐍🐍🐍🐍🐍🐍 Hard Luck , PC Is the Winner 🐍🐍🐍🐍🐍🐍")
            sys.exit("Bye! 👋👋👋👋👋")
            
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main":
    rock_paper_scissors()
     



