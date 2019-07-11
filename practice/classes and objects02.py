#python3.7

class Employee:

    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullName(self):
        return ('{} {}'.format(self.first,self.last))

    def payRaise(self,raise_amt):
        self.pay = int(self.pay * raise_amt)

emp1 = Employee('Ritwik','Gupta',50000)
emp2 = Employee("Ritz","Carlton",90000)




