import random
secretNumber = random.randint(1,100)
print('I have choosen a number between 1 and 100.')
print('Can you guess the number within 7 guesses?')

for guessTaken in range(1,8) :
    print('Make a guess')
    x = int(input())
    if x > secretNumber :
        print('Your guess is too high')
    elif x < secretNumber :
        print('Your guess is too low')
    else :
        break

if x == secretNumber :
    print('Good job! You guesssed my number in ' + str(guessTaken) + ' moves')
else :
    print('Boka***da! Eidao parli na? The number was ' + str(secretNumber))
s = input()
