# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 3:38:29 To 3:57:16
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("********* SCOPE *********")
# Note ::: Viarable working only in sub-scope 
# if it inside sub-scope will not work in higher scope

name = "Sheko" # This in Global Scope
count = 1

def greading():
    color = 'bule' # This is funcion Scope not will work out side function
    #print(name)
    #print(count)
    #note : you cant += for it 
    # name ="hassan" it will be error
    # count +=1 it will be error
    # To solve you should call global vairable
    global count
    count += 3
    global name
    name = "Hassan"
    print(name)
    print(count)
    print(color)
    
def greading_2(name):
    print(name)
    
greading()
greading_2('Shark')
# print(color) # it will be error

print("-------------")

def another():
    greading_2('Mr Hassan')
    
another()
#3.50.38

# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
