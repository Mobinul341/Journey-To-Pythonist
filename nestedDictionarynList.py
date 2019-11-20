'''
#DIctionary Inside dictionary syntax
scientist = {
    'Lui pastore':{
        'First name': 'Lui',
        'Last name':'Pastore',
        'Country':'France'
        },
    'Nicola Tesla':{
        'First name':'Nicola',
        'Last name':'Tesla',
        'Country':'Serbia'
        }
    }

print(scientist)

for scientists, country in scientist.items():
    print("\n\tScientist Name: ", scientists)
    firstName = country['First name']
    secondName = country['Last name']
    location = country['Country']
    print("\nFirst Name: ", firstName, "\nLast Name: ", secondName)
    print("Country: ", location)
'''

#Another Nested Dictionary
pyway = {
    'Kartik': {
        'Name':'Kartik Banik Shishir',
        'Age': 21,
        'Location' : 'Bangla motor'
        },
    'Borshon':{
        'Name':'Un Najmus Sakib Borshon',
        'Age': 20,
        'Location': 'Kalyanpur'
        },
    'Saikat':
    {
       'Name': 'Monoar Salehin Saikat',
       'Age': 19,
       'Location': 'Karwan Bazar'
       },
    'Nabil':{
        'Name':'Sharif Ahmed Nabil',
        'Age': 20,
        'Location': 'Jatrabari'},
    'Raju':{
        'Name': 'Raju Khan',
        'Age': 19,
        'Location':'Uttara'}
    }
#To see Keys and Values in Dictionary inside of a Dictionary
for name, data in pyway.items():
    print("\n\tStudent Name: ", name)
    print("Full Name", data['Name'])
    print("Age: ", data['Age'])
    print("Location: ", data['Location'])

#To see Keys in Dictionary inside of a Dictionary
for names in pyway.keys():
    print(names)

#To see Values in Dictionary inside of a Dictionary    
for info in pyway.values():
    print(info['Name'])
    

    



