class Employee:
    firstname:str ="jyothi"
    lastname:str="korrapati"
    def fullname(self):
        return self.firstname+"  "+self.lastname
emp=Employee()
emp.firstname="sumathi"
print(emp.fullname())
