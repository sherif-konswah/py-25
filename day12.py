# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 5:32:42 To 5:53:29
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("********* Lambda Function *********")

squard = lambda num : num * num

print(squard(2))

#Note it is equal as

def squared(num): return num * num


print(squared(3))


addTwo = lambda num : num + 3

print(addTwo(2))


sum=lambda a,b:a+b

print(sum(2,5))

print('---------You can use in function--------------')
def funcBuilder(X):
    return lambda num : num +X


addTen =   funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

print("=======================================")
print("********* Higher Order Function *********")
# which take function as argment or return function


numbers =[3,7,12,18,22.24]

squared_nums = map(lambda num1 :num1 * num1,numbers)

print(list(squared_nums))

###########################

 
odd_nums = filter(lambda num : num%2 != 0,numbers)

print(list(odd_nums))

#############################
from  functools import reduce


numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr : acc + curr,numbers)
print(total)

totalAfterTen = reduce(lambda acc,curr : acc + curr,numbers,10)
print(totalAfterTen)



names  = ['Sheko','Shark','Alaa','Hassan','Ahmed','Ali']
totalLen = reduce(lambda acc,curr : acc + len(curr),names,0)
print(totalLen)

