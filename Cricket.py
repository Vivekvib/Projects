# Cricket Game

print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~

Instructions:
1. You have to chose between head/tails for the toss.
2. If you won the toss chose bat/bowl.
2. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the two wickets fell or the overs end.
7. The player with maximum runs wins. """)

print("\n---------- Start Game --------")

import random

print("Lets do the toss")
toss_call = input("Chose one head/tail: ").lower()
while ((toss_call!="head") and (toss_call!="tail")):
    toss_call = input("Please check the spelling and chose one from head/tail: ").lower()
toss = ["head", "tail"]
val = random.choice(toss)
P_Runs = 0
P_Wickets = 0
P_Balls = 0
if val == toss_call:                                 #Toss won
    print("Congratulations you won the toss")
    option = (input("Chose what you want to do first bat/bowl : ")).lower()
    while ((option!="bat")and(option!="bowl")):
        option = (input("Please check the spelling and chose what you want to do first bat/bowl: ")).lower()
    if option == "bat":                              #Batting first
        print("Let's start the first innings:")
        while P_Wickets < 2 and P_Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            while not(0<p_chose<7):
                p_chose = int(input("Please Enter a number between 1 to 6 : "))
            c_chose=random.randint(1,6)
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                P_Balls += 1
                P_Wickets += 1
                P_Runs += 0
                print("Score=", P_Runs, "/", P_Wickets)
                print("Balls bowled: ", P_Balls)
            elif p_chose != c_chose:
                P_Balls += 1
                P_Runs += p_chose
                P_Wickets += 0
                print("Score=", P_Runs, "/", P_Wickets)
                print("Balls bowled: ", P_Balls)
        print("Your total Score=", P_Runs, "/", P_Wickets)
        C_Wicket = 0
        C_Run = 0
        C_Balls = 0
        print("Now it's your turn to bowl ")
        while C_Wicket < 2 and C_Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            while not(0<p_chose<7):
                p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                C_Balls += 1
                C_Wicket += 1
                C_Run += 0
                print("Score=", C_Run, "/", C_Wicket)
                print("Balls bowled: ", C_Balls)
            elif p_chose != c_chose:
                C_Balls += 1
                C_Run += c_chose
                C_Wicket += 0
                print("Score=", C_Run, "/", C_Wicket)
                print("Balls bowled: ", C_Balls)
                if C_Run > P_Runs:
                    print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                    break
                elif C_Wicket == 2:
                    print("!!Congratulations you won the match!!")
                    break
            else:
                print("Please provide integer value between 1 to 6")
        if C_Run < P_Runs:
            print("!!Congratulations you won the match!!")
        else:
            pass
    elif option == "bowl":                      #Bowling first
        print("Let's start the game:")
        while P_Wickets < 2 and P_Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            while not(0<p_chose<7):
                p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                P_Balls += 1
                P_Wickets += 1
                P_Runs += 0
                print("Score=", P_Runs, "/", P_Wickets)
                print("Balls bowled: ", P_Balls)
            elif p_chose != c_chose:
                P_Balls += 1
                P_Runs += c_chose
                P_Wickets += 0
                print("Score=", P_Runs, "/", P_Wickets)
                print("Balls bowled: ", P_Balls)
            else:
                print("Please provide integer value between 1 to 6")
        print("Computers total Score=", P_Runs, "/", P_Wickets)
        C_Wicket = 0
        C_Run = 0
        C_Balls = 0
        print("Now it's your turn to bat ")
        while C_Wicket < 2 and C_Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            while not(0<p_chose<7):
                p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                C_Balls += 1
                C_Wicket += 1
                C_Run += 0
                print("Score=", C_Run, "/", C_Wicket)
                print("Balls bowled: ", C_Balls)
            elif p_chose != c_chose:
                C_Balls += 1
                C_Run += p_chose
                C_Wicket += 0
                print("Score=", C_Run, "/", C_Wicket)
                print("Balls bowled: ", C_Balls)
                if C_Run > P_Runs:
                    print("!!Congratulations you won the match!!")
                    break
                elif C_Wicket == 2:
                    print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                    break
                else:
                    pass
        print("Your total Score=", C_Run, "/", C_Wicket)
        if C_Run > P_Runs:
            print("Computer won the match, Better luck next time")
        else:
            pass
    else:
        print("Please provide a correct information: ")
elif val != toss_call:
    print("Computer won the toss and decided to bat first")
    print("Lets begin the first innings")
    while P_Wickets < 2 and P_Balls < 12:
        p_chose = int(input('Enter a number between 1 to 6 : '))
        while not(0<p_chose<7):
                p_chose = int(input("Enter a number between 1 to 6 : "))
        c_chose = random.randint(1, 6)
        print("Your choice is ", p_chose)
        print("Computers choice is ", c_chose)
        if p_chose == c_chose:
            P_Balls += 1
            P_Wickets += 1
            P_Runs += 0
            print("Score=", P_Runs, "/", P_Wickets)
            print("Balls bowled: ", P_Balls)
        elif p_chose != c_chose:
            P_Balls += 1
            P_Runs += c_chose
            P_Wickets += 0
            print("Score=", P_Runs, "/", P_Wickets)
            print("Balls bowled: ", P_Balls)
    print("Computers total Score=", P_Runs, "/", P_Wickets)
    C_Wicket = 0
    C_Run = 0
    C_Balls = 0
    print("Now it's your turn to bat ")
    while C_Wicket < 2 and C_Balls < 12:
        p_chose = int(input("Enter a number between 1 to 6 : "))
        while not(0<p_chose<7):
            p_chose = int(input("Enter a number between 1 to 6 : "))
        c_chose = random.randint(1, 6)
        print("Your choice is ", p_chose)
        print("Computers choice is ", c_chose)
        if p_chose == c_chose:
            C_Balls += 1
            C_Wicket += 1
            C_Run += 0
            print("Score=", C_Run, "/", C_Wicket)
            print("Balls bowled: ", C_Balls)
        elif p_chose != c_chose:
            C_Balls += 1
            C_Run += p_chose
            C_Wicket += 0
            print("Score=", C_Run, "/", C_Wicket)
            print("Balls bowled: ", C_Balls)
            if C_Run > P_Runs:
                print("!!Congratulations you won the match!!")
                break
            elif C_Wicket == 2:
                print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                break
    print("Your total Score=", C_Run, "/", C_Wicket)
    if C_Run < P_Runs:
        print("Computer won the match, Better luck next time")
    else:
        pass