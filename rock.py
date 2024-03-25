import random
print("Let's play the rock,paper,scissor game")
list=['rock','paper','scissor']
p_points=0.0
c_points=0.0
b=0

def game(p_points,c_points,b,list):
    while b<=3:
        b=b+1
        p=input("Enter the input ")
        c=random.choice(list)
        if p == c:
            p_points=p_points+0
            c_points=c_points+0
        elif p == 'rock' and c == 'scissor':
            p_points=p_points+1
            c_points=c_points+0
        elif p == 'scissor' and c == 'rock':
            p_points=p_points+0
            c_points=c_points+1
        elif p == 'paper' and c == 'scissor':
            p_points=p_points+0
            c_points=c_points+1
        elif p == 'scissor' and c == 'paper':
            p_points=p_points+1
            c_points=c_points+0
        elif p == 'rock' and c == 'paper':
            p_points=p_points+0
            c_points=c_points+1
        elif p == 'paper' and c == 'rock':
            p_points=p_points+1
            c_points=c_points+0
    if c_points == p_points:
        print("Its a tie with the opponent as",c_points,"with you as ",p_points)
    elif c_points < p_points:
        print("You won with",p_points)
    elif c_points > p_points: 
        print("You loose with",c_points)
    return None
game(p_points,c_points,b,list)
while True:
    res=input("Do you want to play again?(Y for yes and N for no) ") 
    if res == "Y":
        game(p_points,c_points,b,list)
    else:
        break   





    
