def greeting(name):
    print(f"Hello, {name}!")


name = "Alice"


class Test:
    a = 55


def user_guessing_game(secret_num, stop_chars):
    user_input = ''
    while user_input != stop_chars:
        user_input = input("\nGuess a number from 1 to 100: ")
        if int(user_input) == int(secret_num):
            print("Bingo! You guessed the number")
        else:
            print(f"The number is {user_input}. Try again...")


# user_guessing_game(99, '3')