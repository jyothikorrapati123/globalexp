#globalscope
class Employee:
    firstname:str="jyothi"
    lastname:str="korrapati"
emp=Employee()
print(emp.firstname)
#partially private
class Employee:
    _firstname:str="jyothi"
    _lastname:str="korrapati"
emp=Employee()
print(emp._firstname)
#strictly private scope
class Employee:
    __firstname:str="jyothi"
    __lastname:str="korrapati"
emp=Employee()
print(emp.__firstname)
