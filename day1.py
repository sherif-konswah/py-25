#Course Name 
#Python full course for beginners | complete all-in-one tutorial | 9 hours
#Chanel
#Dave Gray
# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#from vedio start
#Up To 1:20:00 in vedio





#lesson 
greading = 'Hello World!'
print(greading)

# you can commet & Uncomment many line by select lines and SHIFT+/
# Lesson 2
line01 = "******************" # Header / Footer
line02 = "*                *" # Re-use
line03 = "*    Welcome     *" 
line04 ="hghjgkjhghjg"


print('') # Blank Line start
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)


#lesson 3 : opperator
age1 = 9
age2 = 13
print(age1)
print(age1  == age2)
age1+=4

print(age1)
print(age1  == age2)
age1 *=10

print(age1)
print(age1  != age2)
age1/=10

print(age1)
print(age1  < age2)

print(round(age1))
print(age1  >= age2)
print(age1)

x   = True
y = False
z = True

print(not x)
print(not y)
print(x and y)
print(x or y)

print('-------------------------if statement------------------------')

shekoAge = 39
if shekoAge < 10:
    print('He is child')
elif shekoAge < 21:
    print('He is teenager')
else:
    print('He is an adult')

# ternary operator
# one line if statment
print('He is child') if shekoAge < 10 else print('He is not child')


print('*********************************************************************')

#lesson 4 
#String Values

first = 'Sherif'
last ="Roko"

print(type(first))
print(type(first)== str)
print(isinstance(first,str))
# Note the last 2 functions are the same

pizza  = str('Pepperoni')
print(type(pizza))
print(type(pizza)== str)
print(isinstance(pizza,str))

# concatenation
full_name = first +" "+last
print(full_name)
full_name+="!"
print(full_name)

born_decade = 1980

#print(full_name +"Born in " +born_decade)
#you should transfer number to str to concatenate
born_decade =str(born_decade)
print(full_name +"Born in " +born_decade)

print('======================================================================')

multi_line =''' 
 Hi,
 Welcome to python
                         Starting 2020


'''

print(multi_line)

#escaping ' "" ......etc by adding \
print('My nane is sheko , I\'m 30 years')
print('My nane is sheko , \t i live in qatar \n I\'m 30 years')



print('======================================================================')

#String Methods 
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multi_line.title()) # For camel case
print(multi_line.replace("Starting","From"))

print(len(multi_line))

print(len(multi_line.strip()))
print(len(multi_line.rstrip()))
print(len(multi_line.lstrip()))


print('-----------------')
#Build menu
title = "Menu".upper()
print(title.center(30,'='))
print("Coffe".ljust(20,".")+"$1".rjust(4))
print("Cake".ljust(20,".")+"$2".rjust(4))
print("Tea".ljust(20,".")+"$1".rjust(4))
print("Latte".ljust(20,".")+"$3".rjust(4))
print("Muffin".ljust(20,".")+"$4".rjust(4))

print('-----------------')



print(first[1])
print(first[-1])
print(first[1:])
print(first[1:-1])


print(first.startswith('S'))
print(first.endswith("R"))

print(first.isdigit())


print('-----------------')

#Booleans
myBool = True
x = bool(False)

print(type(x) == type(myBool))




print('-----------------')

#Numbers

#Integers
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price,int))

#Float
gpa = 8.234
print(type(gpa))

#Complex 
comp_val = 5+3j
print(type(comp_val))

print(comp_val.real)
print(comp_val.imag)

print('-----------------')

#Built-in Functions For Numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))
print(abs(gpa * -1))



# importing Math class >>>> import math
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# casting string to number
zipcode = "1235"
zip_val = int(zipcode)
print(type(zip_val))
zip_val *= 10
print(zip_val)