import random
game=random.randint(1,100)
num=int(input("enter number"))
c=0
while num!=game:
    if num<game:
        print("guess higher")
    else:
        print("huess lower")   


    num=int(input("enter number"))
    c+=1
 
else:
     print("correct")
     print("you attemp",c)