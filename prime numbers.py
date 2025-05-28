"""This code finds the prime number"""
"""Print True if the number is prime and print False if it is not"""
n= int(input("please enter a number: "))
i=2
flag=True
if n>=2:
    while i<n:
        if n%i==0:
            flag=False
        i+=1
    print(flag)  
else:
    print("The first prime number is two")
