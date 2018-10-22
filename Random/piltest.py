
class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = None

    def assignEmail(self):
        first, last= self.name.split(' ')
        self.email = first + '.' + last + '@gocats.org'
        print("{}.{}@gocats.org".format(first,last))

    def doWork(self, arg):
        pass

name = str(input("What is their name?\n"))
age = int(input("What is their age?\n"))
student1 = Student(name, age)

student1.assignEmail()
