secret_number = 15

attempts = 5
guessed = False

while not guessed and attempts > 0:
    num = int(input('Guess the secret number: '))

    if num == secret_number:
        guessed = True
        print('Yay, guessed')
    else:
        attempts -= 1
    