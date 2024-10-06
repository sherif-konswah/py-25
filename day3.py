# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 1:42:17 To 2:13:47 
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lists

users = ['Sheko','Pop','Ali']

data = ['Sheko',38,True]
emplist = ['S0139']

print("Sheko" in users)
print("Sheko" in data)
print("Sheko" in emplist)

print(users[0])
print(users[-1])

print(users.index('Pop'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(users[0:-1])

print(len(users))
print(users[-len(users):-1])

users.append('Marwan')
print(users)

users += ['Abdo']
print(users)

# # Note adding this
# users += 'Alaa' # It will Storing Letter By Letter
# print(users)

users.extend(['Loka','Zizo'])
print(users)

# You can add list in list
# users.extend(data)
# print(users)

print('----------------------')

users.insert(0,'Sherif')
print(users)

users[2:2] = ['Hassan','Fares']
print(users)
print('----------------------')

# Replace Values
users[1:3] = ['Report','JPL']
print(users)


users[1:3] = ['Report','JPL','Sameh']
print(users)


print('----------------------')
users.remove('Report')
print(users)

#Print Last One Data
print(users.pop())

# Deleting Data Or All List
del users[1]
print(users)
print('----------------------')
print(emplist)
# del emplist
# print(emplist)

# Sorting List

print('----------------------') 
users[1:2]=['ahmed']
print(users)
print('----------------------')
users.sort()
print(users)
print('----------------------')
users.sort(key=str.lower)
print(users)
print('----------------------')
nums = [4,24,42,78,1,5]
print(nums)
nums.reverse()
print(nums)
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# Note above change list item places in sorting
# So If you Want no changing in orignal
print(sorted(nums,reverse=True))
print(nums)

# You Can Take Copy to make edit by many ways
numscopy1= nums.copy()
numscopy2 = list(nums)
numscopy3 = nums[:]
print('----------------------')
print('---- Original-----')
print(nums)
print('---- Coppies-----')
numscopy3.sort()
numscopy2.sort(reverse=True)
print(numscopy1)
print(numscopy2)
print(numscopy3)

print('----------------------')
print('**Other Declearation OF Lists**')
mylist = list([1,'Sheko',True])
print(mylist)


print('----------------------')
print('**Tuples**')
mytuple = tuple(('sheko',42,True))
anothertuple = (1,4,2,8)

print(type(mytuple))
print(type(anothertuple))


print(mytuple)
print(anothertuple)

listtuple = list(mytuple)
listtuple.append('Shark')

print(mytuple)
print(listtuple)
print('---------')
(one,*two,three) = anothertuple

print(one)
print(two)
print(three)
print('---------')
(one,two,*three) = anothertuple

print(one)
print(two)
print(three)

print('---------')
print(anothertuple.count(2))



#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 2:13:48 To :43:07
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Dictionaries
# It is like Java script object

print('----Dictionaries-----')

band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals= "plant",guitar= "page")

print(band)
print(band2)

print(type(band))
print(type(band2))

print(len(band))
print(len(band2))

#Access Items
print(band["vocals"])
print(band.get("vocals"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of keys-values as tuple
print(band.items())


#Virify key exsists
print("guitar" in band)
print("piano" in band)

#change calues
band['vocals'] = "Air"
band.update({"bass": "JPJ"})

print(band)

band2['vocals']="Water"
band2.update(bass="JPL")
print(band2)


#Remove Items
print(band.pop("bass"))
print(band)

band['drums'] = "yeah"
print(band)

#remove last added
print(band.popitem()) # return tuple
print(band)

band['drums'] = "yeah"
print(band)


#delete items
del band["drums"]
print(band)


#clear Data
band2.clear()
print(band2)

del band2

print('-----------------')

#copy dicitionaries
print("** This Good Copies **")
band2 = band.copy()
print(band2)
print(band)

band2["drums"]="ddddd"
print(band2)
print(band)

print("** Or Use This Good Copies **")
band3 = dict(band)



# print("** This Bad Copies **")
# band2 = band
# print(band2)
# print(band)

# band2["drums"]="ddddd"
# print(band2)
# print(band)

print('-----------------')

print("--- Nested Dicitionaries ---")
member1 ={
    "name": "Ali",
    "insturment": "vocals"
}
member2 ={
    "name": "Sheko",
    "insturment": "guitar"
}

band4 = {
    "member1": member1,
    "member2": member2
}

print(band4)
print(band4['member1']["name"])

print(band4.get("member1").get("name"))


# Sets
# It is like Java script object
print('-----------------')
print('----Sets-----')
sets1 = {1,2,3,4}
sets2 = set((1,2,3,4))

print(sets1)
print(sets2)

print(type(sets1))
print(len(sets1))

#No duplicate allowed in sets
sets1 ={1,2,3,3,4}
print(sets1)
# True = 1 & False = 0
sets1 ={1,2,3,4,True,False,0}
print(sets1)

# Check value in set
print(2 in sets1)

#Add new  element to set
sets1.add(8)
print(sets1)

moresets ={99,98,97}
sets1.update(moresets)

print(sets1)

# you can use update with lists , tuples, and dicitionaries
sets1.update(band)
print(sets1)

print("--------------------------")
#Merge two set in new set
one_set = {1,2,3}
two_set = {5,6,7}

merge_set = one_set.union(two_set)
print(merge_set)

#Find Duplicated value in sets
one_set = {1,2,3}
two_set = {3,2,7}

one_set.intersection_update(two_set)
print(one_set)




#Find every value not Duplicated value in sets
one_set = {1,2,3}
two_set = {3,2,7}

one_set.symmetric_difference_update(two_set)
print(one_set)

print('-----------------')
