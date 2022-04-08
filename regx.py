import re

#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# txt ="Demo of regular expressions"
# x= re.search("^Demo", txt)
# if(x):
#     print("Match Successful")
# else:
#     printf("Match not found")

txt = "The rain in 9Spain\
naa\
8"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")