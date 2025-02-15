import random

# Generate a random number
#Loop
    # Ask the user to make a guess
    #if not a valid number
    #   print an error
    # if number  < gues
    #   print too high
    # Else 
    #   Print welll done 


number_to_guess  = random.randint(1,100)
while True: 
    try:
        guess = int(input("guess the number between 1 to 100: "))
        if guess < number_to_guess:
            print("too low!")
        elif guess > number_to_guess:
            print("too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please Enter a Valid Number ")    