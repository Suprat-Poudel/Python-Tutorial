import math
x =float(input("Enter horizontal component (x): "))
g =float(input("Enter acceleration due to gravity (g): "))
v=float(input("Enter initial velocity (v): "))
theta=float(input("Enter angle: "))
y= float(input("position of the ball (y): "))
ans= x*math.tan(theta)-((g*x*x)/(2*v*v*math.cos(theta)*math.cos(theta)))+ y
print(ans)