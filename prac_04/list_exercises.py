numbers = []

for i in range (5):
    number_input = int(input("Number:"))
    numbers.append(number_input)

print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average number is: {sum(numbers)/len(numbers)}")
