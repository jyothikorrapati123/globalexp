#recursive function
lst = []
def fib_recursive(n, a, b,  i):
    if i <= n:
        lst.append(b)
        a = a + b
        b = a - b
        i += 1
        fib_recursive(n, a, b, i)
    else:
        print(lst)
fib_recursive(n=10,a=1,b=0,i=1)
#factiorial by using recursive
def factorial_recursive(num,i,fact):
    if i <=num:
        fact *= i
        i +=  1
        factorial_recursive(num, i, fact)
    else:
        print(fact)
factorial_recursive(num=3, i=1, fact=1)
#prime number by using recursive
def prime_recursive(num,i,res):
    if i <=num:
        if(i!=1 and num%i==0 and i!=num):
            res= False
            i += 1
            prime_recursive(num, i, res)
        else:
            if(res==True):
                print("f{num}is a prime")
            else:
                print("f{num}is not a prime")
prime_recursive(num=13, i=1, res=False)