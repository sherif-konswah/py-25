print('---------------------------------------------')
print("------------ Guess The Number Game--------------")
import sys
import random

def guess_n(name='Player one'):
        
    game_count = 0
    com_wins_count = 0
    player_wins_count = 0


    def play_guess_n():
        nonlocal name
        nonlocal game_count
        nonlocal com_wins_count
        nonlocal player_wins_count

        print('************************************')
        gus1 =int(input(f"{name} : Gues Which Number PC Thinking of ..... 1,2 Or 3:\n\n"))
        gus2 =int(random.choice("123"))

        if(str(gus1) not in {"1","2","3"}):
            print(f"😱😱 {name},You Must Enter Number From 1 To 3 Only!!!!")
            return play_guess_n()
        
        print(f"\n{name} Guesses {str(gus1)}  .")
        print(f"Computer Guesses {str(gus2)}.")
        

        def decide_winner (gus1,gus2):
            nonlocal name
            nonlocal player_wins_count
            nonlocal com_wins_count

            if gus1 == gus2 :
                player_wins_count +=1
                return f"🎉 {name} , You Win " , player_wins_count
            else:
                com_wins_count += 1
                return"🐍 Computer Win ", com_wins_count

            
        game_result = decide_winner(gus1,gus2)
        print(game_result)
        game_count
        game_count +=1

        print(f"\n Game Count : {str(game_count)} \n Total Result  : \n {name}  >>>   {str(player_wins_count)}    \n VS \n PC  >>>      {str(com_wins_count)}")
        print(f"\n {name} Winning Percentage : {str((player_wins_count/game_count))}")
        
        print("\n Play Again??")
        while True:
            playagain = input("\n Y >>> For Yes \n OR \n N >>> For Quit\n")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        if playagain.lower()=="y":
            return play_guess_n()
        else:
            print(" Thank You For Playing Our Game!!!")
            if(player_wins_count == com_wins_count ):
                print ("Final result is Tie")
            elif(player_wins_count > com_wins_count):
                print(f"T🎉🎉🎉🎉🎉🎉 Gongratulation {name}, You Are the Winner T🎉🎉🎉🎉🎉🎉")
            else:
                print("🐍🐍🐍🐍🐍🐍 Hard Luck , PC Is the Winner 🐍🐍🐍🐍🐍🐍")
            
            if __name__ == "__main__":
                sys.exit(f"Bye! {name} 👋👋👋👋👋")
            else:
                return
            
            
    return play_guess_n



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description = "provide a personalized game experiance"
    )



    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True,help="The name of a person to playing the game"
    )




    args = parser.parse_args()

    guess_number = guess_n(args.name)
    guess_number()
        



