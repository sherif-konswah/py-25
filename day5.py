# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 3:05:51 TO 3:29:48
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Functions



# def hello_mr():
#     print("Hello Mr. "+input("Please Enter Your Name : \n"))

# hello_mr()


# def hello_who(gen=input("Mr Or Mrs \n"),name=input("Please Enter Your Name : \n")):
#     print("Hello " + gen +". "+ name)

# hello_who()



def calc_add(num1,num2):
    print(num1+num2)

calc_add(5,7)

    
def r_calc_add(num1=0,num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

print(r_calc_add(5,'uu'))
print(r_calc_add(5,9))
print(r_calc_add())


# infinte args
def multiple_items(*args):
    print(args)
    print(type(args))



multiple_items('ali','hassan')


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first='ali',last='hassan')


print('------------------------------------------')
print('**** Recursion التكرار ****')

def add_one(num):
    if(num >=9):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)

print('-------')
value = "y" # It is mean TRUE
count = 0

while value == "y":
    count += 1
    print(count)
    if(count == 5):
        print("Hi man")
    elif (count == 7):
        value = False
        break
    else:
        continue
    


