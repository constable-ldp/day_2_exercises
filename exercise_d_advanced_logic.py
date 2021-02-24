# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for i in range(1,len(numbers)):
    if numbers[i] == 2 and numbers[i] == numbers[i-1]:
        print(True)
        break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
list_6 = []
list_7 = []
for i in range(len(numbers)):
    if numbers[i] == 6:
        for j in range(i,len(numbers)):
            if numbers[j] == 7:
                list_6.append(i)
                list_7.append(j)
                break
list_6.reverse()
list_7.reverse()

for k in range(len(list_6)):
    del numbers[list_6[k]:list_7[k]+1]
print(sum(numbers))
        

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

for i in range(len(numbers)):
    