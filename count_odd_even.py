
numbers_str = input("Enter a series of numbers separated by commas: ")

number_str_list = numbers_str.split(',')
numbers = []


for num_str in number_str_list:
    num = int(num_str)
    numbers.append(num)


even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
