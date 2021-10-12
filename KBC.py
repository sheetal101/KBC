que=["How many girls in your class",
 "what is capital of uttarakhand",
 "pink city of indai"]
option=[["four", "nine", "seven", "eight"],
["Dehradun", "kotdwara", "dugadda", "Rishikesh"],["Agra", "Jaipur", "Kashmir", "Banglore"]]
solution=[3, 1, 2]
fifty=[["seven", "nine"],["kotdwara","dehradun"],["jaipur", "Rishikesh"]]
answer=[1, 2,1] 
i=0
c=0
while i<len(que):
    print(i+1,que[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j=j+1
    user=int(input("enter your answer: "))
    if user==solution[i]:
        print("Congratulations")
    elif user==5050:
        if c==0:
            k=0
            while k<len(fifty[i]):
                print(k+1,fifty[i][k])
                k=k+1
            c=c+1
            ans=int(input("Choose your Answer"))
            if ans==answer[i]:
                print("Correct Answer")
            else:
                print("wrong answer")
                break
        else:
            print("you have already used lifeline")
            n=int(input("select your answer"))
            if n==solution[i]:
                print("congrats")
            else:
                print("You loss")
    else:
        print("You loss the game")
        break
    i=i+1
    