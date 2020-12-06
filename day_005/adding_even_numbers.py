# Write a program to add all even numbers from 1-100

total = 0

for number in range(0, 101, 2):
    total += number

print(total)