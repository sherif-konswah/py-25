# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 5:17:25 TO 5:32:42
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import sys




print("********* Challege *********")
print(f"This section is proposal game arcade main Menu then open one of two games ")




def play_arcade(name='Player one'):
    welcome_back =False
      
    while True:
            if welcome_back == True:
                print(f"\n {name}, Welcome back to the Arcade menu!!")
            playerchoice =int(input(f"{name} : Pick Your Game ...\n 1 For Rock Paper Scissor Game \n Or 2 For Guess My Number Game \n Or Press X To Exit:\n\n"))
            if(str(playerchoice) not in ["1","2","3"]):
                  print(f"😱😱 {name},You Must Enter Number From 1 To 3 Only!!!!")
                  return play_arcade()
            welcome_back = True
            
            if playerchoice == "1":
                  from day11RPS9 import rps
                  rock_paper_scissors = rps(name)
                  rock_paper_scissors()             
            elif playerchoice == "2":
                  from day11GUES1 import guess_number
                  guess_number = guess_number(name)
                  guess_number()
            else:
                  print("\n See You Next Time")
                  sys.exit(f"Bye! {name} 👋👋👋👋👋")



if __name__ == "__main__":
            
      import argparse
      parser = argparse.ArgumentParser(
      description = "provide a personalized game experiance"
      )



      parser.add_argument("-n", "--name", metavar="name",
      required=True,help="The name of a person to playing the game"
      )




      args = parser.parse_args()     
      play_arcades = play_arcade(args.name)
      # print(f"\n {args.name}, Welcome To The Arcade !!!")
      
      play_arcades(args.name)
                  