import os
import random

# Check if 'words.txt' exists or create it
if os.path.exists('words.txt'):
    print("File found")
else:
    with open('words.txt', "w") as file:
        file.close()
        print("We have created the file, please now add words to it")

# Read words from file
with open("words.txt", "r") as file:
    extract = file.readlines()  # Gets everything in the txt into a list
    line_no = len(extract)  # Finds the number of lines

# Choose a random word from the list
random_line = random.randint(1, line_no - 1)
to_guess = extract[random_line].strip()  # Random word is chosen and strip any extra whitespace
print("The word to guess is:", to_guess)

x = len(to_guess)

hidden = "_" * x  # This will become the all "___" for the user to guess
print(hidden)

used = []


# Function to reveal correct guesses
def reveal_char(guess, to_guess, hidden):
    hidden_list = list(hidden)
    for i, char in enumerate(to_guess):
        if char == guess:
            hidden_list[i] = guess
    return ''.join(hidden_list)


# Main game loop
while "_" in hidden:
    letter = input("Guess ONE Letter: ").lower()
    if len(letter) != 1:
        print("Please enter ONE letter")
    else:
        if letter in used:
            print("You already used", letter)
            print("")
        else:
            used.append(letter)
            print("Used letters:", used)

            if letter in to_guess:
                print("Correct!")
                hidden = reveal_char(letter, to_guess, hidden)
            else:
                print("Incorrect!")

            print("Current word:", hidden)
            print("")

print("Congratulations, you guessed the word:", to_guess)
