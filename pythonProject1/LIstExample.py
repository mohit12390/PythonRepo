userList = ['Mohit','Dinkar','Jeevan','Nana']

print(userList)

#append to the list
userList.append('Paul')
print(userList)

# remove to the list
userList.remove('Paul')
print(userList)

# update to the list
userList[1]='DInakar'
print(userList)

# insert to the list for some index
userList.insert(1,'Sumit')

print(userList)
# delete the user from list
del userList[2]
print(userList)

# count the number of user in the list
print (len(userList))

# sort the list
userList.sort(reverse=True)
print(userList)

userList.pop()
userList.pop()
userList.pop()
userList.pop()

print(userList)
