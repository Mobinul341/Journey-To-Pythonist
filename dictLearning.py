'''
myFavorite = {'color': 'blue',
              'hobby': 'study',
              'genre': ['History', 'Thriller', 'Biography', 'Science', 'Literature'],
              'writer': ['Kazi Nazrul Islam', 'Jashim Uddin', 'Humayun Ahmed']}

print(myFavorite['color'])
print(myFavorite['hobby'])
print(myFavorite['genre'])
print(myFavorite['writer'])
'''

namesNID = {'Rafi': 'Green',
            'Saikat' : 'Sky Blue',
            'Sakib': 'Pink',
            'Nabil': 'Sky Blue',
            'Kartik': 'Black',
            'Raju': 'Sky Blue'}
'''
#Looping Through all KVP
for name, color in namesNID.items():
    print("\nName: ", name, "\nColor: ", color)
'''
'''
#looping through Keys
for name in namesNID.keys():
    print(name)
'''
'''
#looping through Values
for color in namesNID.values():
    print(color)
'''
'''
#Looping through sorted items
for sortedKey, sortedValue in sorted(namesNID.items()):
    print("\nSorted Name: ", sortedKey, "\nSorted Color: ", sortedValue)
'''    

    

