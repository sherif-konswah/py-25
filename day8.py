# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 4:16:17 To 4:39:00
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("********* F-Strings *********")

person = "Sheko"
coins = 3

print("\n "+person + " has "+ str(coins) +" coins lest.")

# Note Concatinate inside "" without + By Useing  %s OR {} 
message = "\n %s has %s coins left" % (person,coins)
print(message)


message2 = "\n {} has {} coins left" .format(person,coins)
print(message2)
# Note Without index you should put as same arrange or you can put index

message3 = "\n {1} has {0} coins left" .format(person,coins)
print(message3)

message4 = "\n {person} has {coins} coins left" .format(coins = coins ,person=person)
print(message4)

# We Can use dicionaries
player = {"person":"Sharko", "coins":6}
message5 = "\n {person} has {coins} coins left" .format(**player)
print(message5)


message8 = f"\n {player['person']} has {player['coins']} coins left"
print(message8)


# Note Short Cut
message6 = f"\n {person} has {coins} coins left"
print(message6)
#note also you can make calc inside
message7 = f"\n {person.lower()} has {2*4} coins left"
print(message7)

print("---------------")
## you can use also options 
num = 10
print(f"\n2.25  times {num} is {2.25 * num:.2f}")
# make also in loop
for num in range(1,11):
    print(f"\n2.25  times {num} is {2.25 * num:.2f}")
    
for num in range(1,11):
    print(f"\n{num} Divided By 4.52 {num/4.52:.2%}")
    

# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
