import math
A=float(input("Enter Amount: "))
P=float(input("Enter Principle: "))
T=float(input("Enter Time: "))
ans= A*pow(1+P/100, T)
print("Total Sum:", ans)