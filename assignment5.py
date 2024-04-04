#Write a program to print numbers from 1 to 0, but stop if the number is 5.
number = 1
while number <= 10:
    if number == 5:
        break  
    print(number)
    number += 1
    
#Write a program to iterate through a list and stop when encountering a specific element.
my_list = [1, 2, 3, 4, 5, 6, 7]
stop_element = 5

for element in my_list:
    if element == stop_element:
        break  
    print(element)
    
#Write a program to skip printing even numbers from  1 to 10.
for number in range(1, 11):
    if number % 2 == 0:
        continue  
    print(number)
    
#Write a program to print numbers from 0 to 9 using range().
for number in range(10):
    print(number)
    
#Write a program to print multiplication tables from  to 5, but stop after the first table is printed for each number
for i in range(1, 6):
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()
        
#Write a program to skip printing even numbers using a while loop
number = 0

while number < 10:
    number += 1  
    if number % 2 == 0:
        continue  
    print(number)