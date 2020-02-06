Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def do_simple_func(simple_list, empty_list):
	while simple_list:
		new_list = simple_list.pop()
		print("Popping List elements are: "+ new_list)
		empty_list.append(new_list)

		
>>> def show_list(empty_list):
	for showing in show_list:
		print("\nPrinting the Empty List: "+showing)

		
>>> simple_list = ['Borshon', 'Kartik', 'Delowar', 'Raju']
>>> empty_list = []
>>> do_simple_func(simple_list, empty_list)
Popping List elements are: Raju
Popping List elements are: Delowar
Popping List elements are: Kartik
Popping List elements are: Borshon
>>> show_list(empty_list)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    show_list(empty_list)
  File "<pyshell#9>", line 2, in show_list
    for showing in show_list:
TypeError: 'function' object is not iterable
>>> def show_list(empty_list):
	for showing in empty_list:
		print("\nPrinting the Empty List: "+showing)

		
>>> show_list(empty_list)

Printing the Empty List: Raju

Printing the Empty List: Delowar

Printing the Empty List: Kartik

Printing the Empty List: Borshon
>>> 
