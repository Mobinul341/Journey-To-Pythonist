
>>> def faluda(*food_items):
	print("The Food items for Faluda: ", food_items)


>>> faluda("Apple")
The Food items for Faluda:  ('Apple',)
>>> faluda("Banana", "Milk", "Ruh-Afza", "Noodles", "Ice cream")
The Food items for Faluda:  ('Banana', 'Milk', 'Ruh-Afza', 'Noodles', 'Ice cream')
>>> 
>>> 
>>> def faluda(*desert_items):
	print("\nHere is all the items used in Faluda: ")
	for used in desert_items:
		print(">> "+used)

		
>>> faluda("Cherry")

Here is all the items used in Faluda: 
>> Cherry
>>> faluda("Mango", "Grape", "Rose water")

Here is all the items used in Faluda: 
>> Mango
>> Grape
>> Rose water
>>> 
>>> 
>>> 
>>> def juice(glass, *fruits):
	print("Number of glass", int(size),"\nThe fruits you want to mix up: ")
	for fol in fruits:
		print(">> "+fol)

		

>>> 
>>> def juice(glass, *fruits):
	print("Number of glass", int(glass),"\nThe fruits you want to mix up: ")
	for fol in fruits:
		print(">> "+fol)

		
>>> juice(5, "Mango")
Number of glass 5 
The fruits you want to mix up: 
>> Mango
>>> juice(8, "Orange", "Lemon", "Coriandar", "Suger")
Number of glass 8 
The fruits you want to mix up: 
>> Orange
>> Lemon
>> Coriandar
>> Suger
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def nums(*int_inputs):
	print("The number you have inserted here: ", int_inputs)

	
>>> nums(5)
The number you have inserted here:  (5,)
>>> nums(7,8,9,4,6,3,2,1)
The number you have inserted here:  (7, 8, 9, 4, 6, 3, 2, 1)
>>> 
>>> 
>>> def zoo(*animals):
	print("\nThe animal you have entered here is: ")
	for anime in animals:
		print("** "+anime)

		
>>> zoo('tiger')

The animal you have entered here is: 
** tiger
>>> zoo('Monkey', 'Rhino', 'Croc', 'Snake')

The animal you have entered here is: 
** Monkey
** Rhino
** Croc
** Snake
>>> 
>>> 
>>> def travel(ticket, *places):
	print("\nHow many ticaket do you want to buy", int(ticket), "\nWhere do you want to go: ")
	for jaiga in places:
		print(">> "+jaiga)

		
>>> travel(5, "Dhaka")

How many ticaket do you want to buy 5 
Where do you want to go: 
>> Dhaka
>>> travel(7, "Bandarban", "Rangamati", "Khagrachori", "Neelgiri")

How many ticaket do you want to buy 7 
Where do you want to go: 
>> Bandarban
>> Rangamati
>> Khagrachori
>> Neelgiri
>>> 
