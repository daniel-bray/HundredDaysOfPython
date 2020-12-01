# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

true_count = 0
love_count = 0

for letter in "true":
    true_count += lower_name1.count(letter)
    true_count += lower_name2.count(letter)

for letter in "love":
    love_count += lower_name1.count(letter)
    love_count += lower_name2.count(letter)

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
