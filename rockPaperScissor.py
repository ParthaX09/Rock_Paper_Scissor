from random import randint
choice=['rock','paper','scissor']
man=0
comp=0
print("---ROCK-PAPER-SCISSOR---")
print("---INSTRUCTIONS:Input either rock paper or scissor...")
points=int(input("How many points you wnat to play for:"))
while(1):
    name=input("Name:")
    while(1):
        if man==points or comp==points:
            break
        inp=input(">>").lower()
        oppo=choice[randint(0,10000)%3]
        print(f"you={inp}  Computer={oppo}")
        if inp==oppo:
            man+=0
            comp+=0
        elif inp=='rock':
            if oppo=='paper':
                comp+=1
            if oppo=='scissor':
                man+=1
        elif inp=='paper':
            if oppo=='rock':
                man+=1
            if oppo=='scissor':
                comp+=1
        elif inp=='scissor':
            if oppo=='rock':
                comp=+1
            if oppo=='paper':
                man+=1 
        else:
            print("Wrong input...Please enter again")
            continue
    print(f"{name}={man}------Computer={comp}")
    if man>comp:
        print("---YOU WIN---")
    elif man<comp:
        print("---YOU LOSE---")
    else:
        print("---DRAW---")
    man,comp=0,0
    run=input("do you wish to go for another round[yes/no]:")
    if run.lower()=='yes':
        continue
    if run.lower()=='no':
        print("---GAME OVER---")
        break  