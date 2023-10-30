import random
number_of_guesses = 0
comp = random.randint(0, 100)
while True:
    myguess = int(input("Guess a number from 1 to 100: "))
    if(0<= myguess <= 100):
        if(myguess == comp):
            number_of_guesses += 1
            print(f"You guessed the correct number in your {number_of_guesses} attempt")
            break
        elif(myguess>comp):
            number_of_guesses += 1
            print("Lower number please")
        elif(myguess<comp):
            number_of_guesses += 1
            print("Higher number please")
    else:
        print("Please only choose a number from only 1 to 100 (not less than 1 and also not more than 100)")
        number_of_guesses += 1