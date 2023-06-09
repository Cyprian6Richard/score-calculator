# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x<y:
#     print ("x is less than y")

# elif x==y:
#     print("x is equal to y")
# else:
#     print("xis greater than y"

#enter scores per subject
math= int(input("Enter math score"))
english= int(input("Enter english score"))
kiswahili= int(input("Enter kiswahili score"))
socialstudies= int(input("Enter social studies score"))

#calculate total marks
score=math+kiswahili+english+socialstudies
#get average
average=score/4
print(score)
print(average)

if average >=80:
   print("you scored an A")
elif average >= 70 and average <= 79:
   print("you scored a B")
elif average >=60 and average==69:
   print("you scored a C")
elif average >=50 and average==59:
   print("you scored a D")
elif average >=40 and average==49:
   print("you scored an E")
elif average <40:
   print("you scored an F")



