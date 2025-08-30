def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

------------------------------------------------
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random


randomnum = random.randint(1,100)
usernum = -1
counter =0
def Check_number(randomnum):
    global usernum
    usernum = input("Enter number")
    if int(usernum) == int(randomnum):
        return f"match"
    if int(usernum) < int(randomnum):
        return "too low"
    if int(usernum) > int(randomnum):
        return "too high"
        
level = input("type 'Hard' or 'Easy'")
if level == "Hard":
    counter = 5
elif level == "Easy":
    counter = 10
    
for i in range(counter):
    result = Check_number(int(randomnum))
    if result == "match":
        print(f"your selection{usernum} math with computer selection {randomnum}")
        break
    if result == "too low":
        print(f"too low.. try again")
        continue
    if result == "too high":
        print(f"too high.. try again")
        continue
    else:
        print("you lost")
                 
