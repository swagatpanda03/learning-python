#guessing game
secretNumber = 9
guessLimit = 3
guessCount = 0

while guessCount < guessLimit:
    guess = int(input('Guess: '))
    if guess == secretNumber :
        print('You Guessed right')
        print('You Won')
        break;
    elif guess < secretNumber:
        print('Choose a larger number')
        guessCount += 1
    elif guess > secretNumber and guessCount < guessLimit - 1:
        print('Choose a smaller number')
        guessCount += 1
    else:
        print('You Lost!')
        break
