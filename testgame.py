print("Hello welcome to my game")
ans = input ("are you ready to play yes/no")
score = 0

if ans.lower() == "yes":
    ans = input("1. what is my name? ")
    if ans.lower() == "pablo":
        score += 1
        print("correct")
    else:
        print("wrong")
        
    ans = input("1. what is my age? ")
    if ans.lower() == "33":
        score += 1
        print("correct")
    else:
        print("wrong")
        
    ans = input("1. what is my pets name? ")
    if ans.lower() == "peanut":
        score += 1
        print("correct")
    else:
        print("wrong")

    ans = input("1. what is my wifes name? ")
    if ans.lower() == "petra":
        score += 1
        print("correct")
    else:
        print("wrong")

print(score)
