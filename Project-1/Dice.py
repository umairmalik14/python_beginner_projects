import random

#Loop => we put everything is inside loop for repetations of infinite loop. 
# Ask: roll the dice?
 # if users enter Y
    #   Generate two random numbers
    #     print them
    # if user enters n 
    #    print user Thank you message
    #    Terminate 
    # else 
    #     print invalid choice
while True: 
    choice =  input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else: 
        print('Invalid Choice')    


