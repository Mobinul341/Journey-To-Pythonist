#skip range
evenNumbers = list(range(1,11,2))
print(evenNumbers)

#Basic statistical functions
digits = [23,21,25,14,45,87,95,74,36,51,15,122,10,98]
print(sum(digits),'\n', max(digits), '\n', min(digits))

#Create a set of number with range() and square it
square = []
for value in range(1,11):
    squares = value**2
    square.append(squares)
print(square)


#list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

#list slicing
footballer = ['Messi', 'Ronaldo', 'Neymar', 'Salah', 'Mane', 'Aguero', 'Hazard']

#print first 3 index from footballer list
print(footballer[:3])

#print after first 4 index from footballer list
print(footballer[3:])

#print specific range index from footballer list
print(footballer[2:4])

#loop through slice
for player in footballer[:2]:
    print(player.upper())

#Copying into another list
socceroose = footballer[:]
print(socceroose)


    
