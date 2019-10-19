#Some Lists to use operations
mixedList = ['Nabil', 2, 'Mamun', 3,3, 'Borshon', 3.45, 'Deluar', 5, 'Khairul', 5.5]
mixedList2 = ['Nabil', 2, 'Mamun', 3,3, 'Borshon', 3.45, 'Deluar', 5, 'Khairul', 5.5]
mixedList3 = ['Nabil', 2, 'Mamun', 3,3, 'Borshon', 3.45, 'Deluar', 5, 'Khairul', 5.5]
oneList = ['Niam', 'Main']
intList = [1,4,67,78,98,123,45,65,32,12,145,127]

#Length of List
print(len(mixedList))

#Print by Index and Check the Index
print(mixedList[0], '\n', mixedList[4])
print(mixedList.index('Deluar'))

#Append single data in List using append()
mixedList.append('Bihon')
mixedList.append(5)
print(mixedList)

#Remove last data of the list using pop()
mixedList.pop()
print(mixedList)
mixedList.pop()
print(mixedList)

#Count any data how many in a List using count()
print(mixedList.count(3))

#Remove any data by calling the exact data using remove()
mixedList.remove(3)
print(mixedList)

#Clearing whole list data using clear()
mixedList2.clear()
print(mixedList2)

#Also clearing whole list using del keyword
del mixedList3[:]
print(mixedList3)

#Extending data in a list, it will take iterable or large string data which will split into multiple data in the end using extend()
mixedList.extend('500')
print(mixedList)

#Inserting data into a specific Index using insert()
mixedList.insert(0,'Moon')
print(mixedList)

#Reverse whole list using reverse()
oneList.reverse()
print(oneList)

#Sorting data in Ascending to descending and Reverse way using sort()
intList.sort()
print(intList)
intList.sort(reverse=True)
print(intList)



















