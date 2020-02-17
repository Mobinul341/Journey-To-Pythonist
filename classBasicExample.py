class Kptech():
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill

    def greetings(self):
        print("%s, Hello from KPTech Pyway learning."%self.name)

    def skill_on_age(self):
        if self.age<=12:
            print("%s, Your age is %d\nYour skill is %s\nYou are recommanded Python basic with problem solving"%(self.name.upper(), self.age, self.skill))
        elif self.age>12 and self.age<=20:
            print("%s, Your age is %d\nYour skill is %s\nYou are recommanded Python intermediate with problem solving and file handling"%(self.name.upper(), self.age, self.skill))
        elif self.age>20 and self.age<35:
            print("%s, Your age is %d\nYour skill is %s\nYou are recommanded Python professional with software development and data science"%(self.name.upper(), self.age, self.skill))
        else:
            print("%s, Your age is %d\nYour skill is %s\nYou are recommanded to retire from coding profession."%(self.name.upper(), self.age, self.skill))


firstPerson = Kptech("Kartik", 21, "C++")
print("Hello, %s from KPtech, you are %d years old and you know %s."%(firstPerson.name.upper() , firstPerson.age, firstPerson.skill))

firstPerson.greetings()
firstPerson.skill_on_age()


secondPerson = Kptech("Saikat", 36, "Java")
secondPerson.skill_on_age()

