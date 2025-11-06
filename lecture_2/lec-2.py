#exercise 1
#identify small from 3 numbers
n1=input("enter na")
n2=input("enter na")
n3=input("enter na")
print(n1,n2,n3)
if n1<n2 and n1<n3:
    print(n1)
elif n2<n1 and n2<n3:
    print(n2)
else:
    print(n3)        