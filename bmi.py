height= float(input("Enter height(in mtrs):"))
weight= float(input("Enter weight(kg):"))
bmi= float(weight/(height*height))
print("BMI : ",bmi)
if bmi<= 18.5:
    print("Underweight")
elif bmi>18.5 and bmi<24.9:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Obese")
else:
    print("Invalid Input")

