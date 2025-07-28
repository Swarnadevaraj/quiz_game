
print("welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :) ")
score=0 

answer= input("What doese cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer= input("Who is full form of TN? ")
if answer.lower()== "Tamil Nadu":
    print("Correct!")
    score+=2

else:
    print("Incorrect!")


answer= input("What doese ROM stands for? ")
if answer.lower() == "Read Only Memory":
    print("Correct!")
    score+=3
else:
    print("Incorrect!")



answer= input("What doese RAM stands for? ")
if answer.lower() == "central Random Access Memory":
    print("Correct!")
    score+=4
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct ")
print("you got " + str((score/4)*100 ) + " percentage")