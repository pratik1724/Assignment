#Print number from 1 to 5 uing a while loop.
counter = 1

while counter <= 5:
    print(counter)
    counter += 1
    
#Calclate the sum of numbers from 1 to 10 using a while loop.
total = 0
counter = 1

while counter <= 10:
    total += counter  
    counter += 1
    
#Calclate the factorial of a number using a for loop.
def factorial(n):
    result = 1  
    for i in range(1, n + 1):
        result *= i  
    return result

#Count the number of vowels in a string using a for loop.
def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

#Print a pattern using nested loop.
size = 5
for i in range(size):
    for j in range(i + 1):
        print("*", end=" ")
    print() 
    
#Generate a mltiplication table using nested loop.
size = 10
for i in range(1, size + 1):
    for j in range(1, size + 1):
        result = i * j
