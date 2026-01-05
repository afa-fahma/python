# 1. Write a function that takes a number as input and returns whether the
# number is even or odd.

# def evenorodd(number):
#     if number %2==0:
#         return "even"
#     else:
#         return "odd"
# print(evenorodd(4))
# print(evenorodd(7))

# 2. Write a function that takes three numbers as input and returns the largest
# number among them.
# def largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b >= a and b >=c:
#         return b
#     else:
#         return c
# print(largest(10,25,15))   

# 3. Write a function that takes a list of numbers as input and returns the sum of
# all elements in the list.
# def abc(numbers):
#     total=0
#     for num in numbers:
#         total +=num
#     return total
# print(abc([1,2,3,4,5]))

# 4. Write a function that takes a list of numbers as input and returns a new list
# containing only even numbers.
# def get_even_numbers(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(get_even_numbers(nums))

# 5. Write a function that takes a string as input and returns the length of the
# string.
# def string_length(text):
#     return len(text)
# word = "Hello World"
# print(string_length(word))

# 6. Write a function that takes a string as input and returns the string in
# uppercase.
# def to_uppercase(text):
#     return text.upper()
# word = "hello world"
# print(to_uppercase(word))


# 7. Write a function that takes a number as input and returns whether the
# number is positive, negative, or zero.
# def check_number(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"
# print(check_number(10))  
# print(check_number(-5))  
# print(check_number(0))    



# 8. Write a function that takes a number as input and returns True if the number
# is a multiple of both 3 and 5, otherwise returns False .
# def is_multiple_of_3_and_5(num):
#     return num % 3 == 0 and num % 5 == 0
# print(is_multiple_of_3_and_5(15)) 
# print(is_multiple_of_3_and_5(9))  
# print(is_multiple_of_3_and_5(10))  


# 9. Write a function that takes a list of numbers as input and returns the
# maximum value in the list.
# def find_max(numbers):
#     return max(numbers)
# print(find_max([3, 7, 2, 9, 5]))  
# def find_max(numbers):
#     maximum = numbers[0]
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#     return maximum

# 10. Write a function that takes marks as input and returns the grade according
# to the following rules:
# A for marks ≥ 90
# B for marks ≥ 75
# C for marks ≥ 60
# Fail for marks below 60
# def get_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     else:
#         return "Fail"
# print(get_grade(92))  
# print(get_grade(80)) 
# print(get_grade(65)) 
# print(get_grade(50))  



# 11. Write a function that takes a price as input and returns the discounted
# price after applying a 10% discount.
# def discounted_price(price):
#     discount = price 
#     return price - discount
# print(discounted_price(100)) 


# 12. Write a function that takes a list of numbers as input and returns the count
# of even and odd numbers.
# def count_even_odd(numbers):
#     even_count = 0
#     odd_count = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#     return even_count, odd_count
# nums = [1, 2, 3, 4, 5, 6]
# even, odd = count_even_odd(nums)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 13. Write a function that takes a temperature in Celsius as input and returns
# the temperature in Fahrenheit.
# def c_to_f(celcious):
#     return(celcious*9/5)+32
# print("temperature in fahrenheit:",c_to_f(38))


# num=int(input("enter a number:"))
# def factorial(n):
#     factorial=1
#     if n<=0:
#         print("null")
#     else:    
#      for i in range(1,n+1):
#         factorial=factorial*i
#      return factorial 
# print(factorial(num))  


# def tailfactorial(n,accumulator=1):
#     if n==0 or n==1:
#         return accumulator
#     else:
#         return tailfactorial(n-1,accumulator*n)
# print(tailfactorial(5))






        
    



