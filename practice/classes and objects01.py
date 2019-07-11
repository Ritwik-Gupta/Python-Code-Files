#python3.7

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullName(self):
        return ('{} {}'.format(self.first,self.last))

    def payRaise(self,raised):
        self.pay = int(self.pay * raised)

emp1 = Employee('Ritwik','Gupta',50000)
emp2 = Employee("Ritz","Carlton",90000)


