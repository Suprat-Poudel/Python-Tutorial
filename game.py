print("ROCK, SCISSOR,PAPPER ")
print("1 is Rock")
print("2 is Scissor")
print("3 is Papper")

p1=int(input("Enter Player 1: "))
p2=int(input("Enter Player 2: "))

if p1==1 and p2==1:
    print("Draw")
if p1==2 and p2==2:
    print("Draw")
if p1==3 and p2==3:
    print("Draw")
if p1==1 and p2==2:
    print("Player A wins")
    print("Player B losses")
if p1==1 and p2==3:
    print("Player B wins")
    print("Player A losses")
if p1==2 and p2==1:
    print("Player B Wins")
    print("Player A losses")
if p1==2 and p2==3:
    print("Player A wins")
    prinnt("Player B losses")
if p1==3 and p2==1:
    print("Player B losses")
    print("Player A wins")
else:
    print("Invalid")

