# Program to find whether a student is passed or failed
# coditions
# should score >33 in each subject
# total > 33
m1 = (input("Enter the marks"))
m2 = (input("Enter the marks"))
m3 = (input("Enter the marks"))
avg = (m1+m2+m3)
if(m1 < 33 or m2 < 33 or m3 < 33):
    if(avg <= 40):
        print("The student failed")
else:
    print("Passed")


