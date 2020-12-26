import random
word_list = ['aardvark', 'babboon', 'camel']
display = ""
chosen_word = random.choice(word_list)
print(f"pssst the chosen word is {chosen_word}")

player_guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == player_guess:
        display += letter
    else:
        display += "_"

print(display)

