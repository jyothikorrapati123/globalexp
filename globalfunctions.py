#globalvariable
def fullname():
    global  fname
    lname ="prasad"
    fname ="devisri"
fullname()
print(fname)
"""print(lname)"""#throw an error


#functionalscope
def fullname():
    global  lname
    lname ="prasad"
    fname ="devisri"
fullname()
print(fname)
print(lname)


