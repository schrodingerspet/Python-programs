import random
toss= [0,1]
choice = random.choice(toss)
n=int(input ("Enter 0 for Heads & 1 for Tails:"))
while n not in toss:
    n=int(input('Please enter a valid number! Enter any number between 0 to 1 only:'))
if n==choice:
    print("You won!")
    k1=int(input("Enter 0 for Bowling & 1 for Batting:"))
    while k1 not in toss:
        k1=int(input('Please enter a valid number! 0 or 1!!'))
    print("You chose", k1 , "!")
    k2=1-k1
elif n!=choice:
    print("Sorry, you lost! The computer decides...")
    k2=random.choice(toss)
    print("Computer chose",k2, "!")
    k1=1-k2

#Game part starts here
numbers=[0,1,2,3,4,5,6]
s=0
s1=0
if k1==0:
    print('You are Bowling First!')
    while True:
        ball=int(input('Enter any number between 0 to 6:'))
        while ball not in numbers:
            ball=int(input('Invalid Input!!Please enter any number between 0 to 6 only:'))
        bat=random.choice(numbers)
        if ball!=bat:
            s=s+bat
            print('Computer has made:', s , 'runs')
        else:
            print('Out!')
            print('You have to make:',s+1,'runs to win!')
            break
    print('Now, you are batting!')
    
    z=0
    while True:
        bat=int(input('Enter any number between 0 to 6:'))
        while bat not in numbers:
            bat=int(input('Invalid Input!!Please enter any number between 0 to 6 only:'))
        ball=random.choice(numbers)
        if bat!=ball:
            if s>s1:
                s1=s1+bat
                print('You have made:', s1, 'runs')
                print('Another', (s-s1)+1, 'runs to win!')
            else:
                z=1
                break
        else:
            print('Out!')
            break
    if z==0:
        print('Sorry, you lost!')
    else:
        print('You Win!')
else:
    print('You are Batting First!')
    
    while True:
        bat=int(input('Enter any number between 0 to 6:'))
        while bat not in numbers:
            bat=int(input('Invalid Input!! Please enter any number between 0 to 6 only:'))
        ball=random.choice(numbers)
        if ball!=bat:
            s=s+bat
            print('You have made:', s , 'runs')
        else:
            print('Out!')
            print('Computer needs:',s+1,'runs to win!')
            break
    print('Now, you are balling!')
    
    
    z=0
    while True:
        ball=int(input('Enter any number between 0 to 6:'))
        while ball not in numbers:
            ball=int(input('Invalid Input!!Please enter any number between 0 to 6 only:'))
        bat=random.choice(numbers)
        if bat!=ball:
            if s>s1:
                s1=s1+bat
                print('Computer has made:', s1, 'runs')
                print('Computer needs another', (s-s1)+1, 'runs to win!')
            else:
                z=1
                break
        else:
            print('Out!')
            break
    if z==0:
        print('You Win!')
    else:
        print('Computer wins!')