import random
wds = ['jail','cage','prison','containment']
w = random.choice(wds)
body_stage = ["""
                             ________
                            |        |
                            |        
                            |
                            |
                            |
                            |
                            |
                            |
                        ____|____        
            
            """,       
            """
              
                             ________
                            |        |
                            |        0
                            |
                            | 
                            |
                            |
                            |
                            |
                        ____|____        
             """,
             """ 
                             ________
                            |        |
                            |        0
                            |        |
                            |        |
                            |
                            |
                            |
                            |
                        ____|____        
            """,
            """
                             ________
                            |        |
                            |        0
                            |        |
                            |        |
                            |        |
                            |        |
                            |
                            |
                        ____|____        
            """,
            """
                             ________
                            |        |
                            |        0
                            |       _|
                            |        |
                            |        |
                            |        |
                            |
                            |
                        ____|____        
            """,
            """
                             ________
                            |        |
                            |        0
                            |       _|_
                            |        |
                            |        |
                            |        |
                            |       
                            |
                        ____|____        
            """,
            """
                             ________
                            |        |
                            |        0
                            |       _|_
                            |        |
                            |        |
                            |        |
                            |       / 
                            |
                        ____|____        
            """,
            """
                             ________
                            |        |
                            |        0
                            |       _|_
                            |        |
                            |        |
                            |        |
                            |       / \
                            |
                        ____|____        
            """
        ] 
count = len(w)
j=count-1
word=''
for alpha in w:
    guess = input("Enter the guess: ")
    if alpha == guess:
        word = word+guess
    else:
        print("Incorrect!!! HANGMAN APPEARS!!!! AND GIVE YOU 8 CHANCES...")
        for i in range(0,8):
            print("Hangman stage :",i+1 ,body_stage[i])
            g=input("guess again")
            if alpha == g:
                word = word+g
                print("Out of Danger and hangman")
                break
    if len(word) != 0:
        print(word.upper(),' _ '*j)
        j=j-1
    else:
        break
if len(word) != len(w):
    print("You loose.")
else:
    print("You won. The word is: ",word.upper())