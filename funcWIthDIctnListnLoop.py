
#Function with while loop 
def club_invite(name, age):
    entry = name, '\n' , age
    return entry

while True:
    user = input("Enter your name: ")
    boyosh = int(input("Enter your age: "))

    if boyosh<18:
        break
    else:
        member = club_invite(user, boyosh)
        print("Hello member: ", member)


#Passing a list into parameter
def kptech_members(names):
    for nam in names:
        print("\nHello : ", nam.upper())
    
member = ['raju', 'nabil', 'kartik', 'rafi', 'mamun']
kptech_members(member)


#Returning into a dictionary
def kptech_dict(name, serial):
    kptech = {
        "Username": name,
        "ID":serial
    }
    return kptech

kps = kptech_dict('Raju', 21)
print("Welcome to kptech Mr.",kps["Username"],"\nyour Roll is: ",kps["ID"])



