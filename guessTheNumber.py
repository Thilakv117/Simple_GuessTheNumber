import random
random_number = random.randint(1,50)
count = 0
number_of_tries = 5
while True:
    count += 1
    try:
        user_guess = int(input("Enter the number: "))
    except ValueError:
        print("Enter the number in int")
    if user_guess == random_number:
        print("You Guessed it Correctly!")
        break
    elif user_guess < random_number:
        print("Low")
    elif user_guess > random_number:
        print("High")
    print("You Guseed it Wrong!")
    print(f"Number of tries left - {number_of_tries - count}")
    if count == number_of_tries:
        print("Try next time")
        print("The Correct answer is", random_number)
        break

    