import random
word_list = ['aardvark', 'babboon', 'camel']
display = []
chosen_word = random.choice(word_list)
print(f"pssst the chosen word is {chosen_word}")


for _ in range(len(chosen_word)):
    display+="_"


print(display)


player_guess = input("Guess a letter: ").lower()


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == player_guess:
        display[position] = letter


print(display)

