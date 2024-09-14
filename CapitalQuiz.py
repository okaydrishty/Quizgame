print("Capitals of the World-QUIZ")
start=input("Do you want to play? ")
if start.lower()!= "yes":
    print("game over")
    quit()
print("Lets go")
name= input("enter your name ")
print("HI",name,"If you answer correctly you gain +10 and -5 for incorrect")
score=0
conti=input("Choose your continent:Asia/ Europe ")
if conti.lower()=="asia":
    ans=input("What is the capital of India ")
    if ans.lower()=="delhi":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)
    
    ans=input("What is the capital of Indonesia ")
    if ans.lower()=="jakarta":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)

    ans=input("What is the capital of Bhutan ")
    if ans.lower()=="thimphu":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)
elif conti.lower()=="europe":
    ans=input("What is the capital of Frace ")
    if ans.lower()=="paris":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)
    
    ans=input("What is the capital of Germany ")
    if ans.lower()=="berlin":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)

    ans=input("What is the capital of Czechia ")
    if ans.lower()=="prague":
        print("correct")
        score+=10
    else:
        print("incorrect")
        score-=5
    print("score:",score)
else: 
    print("invalid name")
    quit()
print("GAME OVER \n YOU SCORED", score)