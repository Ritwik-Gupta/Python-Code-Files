#python3.7

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@' + 'company.com'
        self.pay = pay

    def name(self):
        self.fullname = self.first + " " + self.last
        return(self.fullname)

    def applyRaise(self,raiseAmt):
        self.pay = self.pay*(1+raiseAmt/100)

emp1 = Employee('Ritwik','Gupta',50000)
