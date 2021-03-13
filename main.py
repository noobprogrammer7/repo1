# # to find the greatest number among the three numbers
n1 = int(input("pls enter the first number:\n"))
n2 = int(input("pls enter the second number:\n"))
n3 = int(input("pls enter the third number:\n"))

if(n1>n2 and n3):
    print(n1, "is the largest number")
else:
    print(n2, "is the largest number")

if (n2>n1 and n3) :
    print(n2, "is the largest number")
else:
    print(n3, "is the largest number")
