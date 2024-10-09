# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 6:12:28 To  6:24:17
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class JustNotCoolError(Exception):
    pass


print("********* Exceptions & Errors *********")

x = 2
try:
    print( x / 1)
except NameError:
    print("Name Error Means Something is undefined") 
except ZeroDivisionError:
    print("Please Don't devide on zero")
else:
    print("no error")
finally:
    print("Print With Or Without An Error")


print('----------------------')

try:
    print( x / 0)
except Exception as error:
    print(error)





try:
    if not type(x) is str:
        raise TypeError("Only String Are Allowed")
except Exception as error:
    print(error)




try:
    raise Exception("Only String Are Allowed")
except Exception as error:
    print(error)



try:
    raise JustNotCoolError("Only String Are Allowed")
except Exception as error:
    print(error)