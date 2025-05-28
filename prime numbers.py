"""This code finds the prime number"""

n= int(input("please enter a number: "))
i=2
flag=True
if n>=2:
    while i<n:
        if n%i==0:
            flag=False
        i+=1
if flag:
    print("It's a prime number")
else:
    print("It is not a prime number")  
else:
    print("The first prime number is two")
