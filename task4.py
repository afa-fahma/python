# 1. Write a program to check whether a number is positive, negative, or zero.
# a=5
# if a > 0:
#     print("The number is positive.")
# elif a < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# # 2. Check if a number is even or odd.
# b=10
# if b%2==0:
#     print("b is even")
# else:
#     print("b is odd")

#3. Given a number, check if it is greater than 100.
# c=39
# if c>100:
#     print("c is greater than 100")
# else:
#     print("c is not greater than 100")        

#4. Check whether a person is eligible to vote (age ≥ 18).
# age=20
# if age >= 18:
#     print("Eligible for vote.")
# else:
#     print("not eligible for vote.")

#5. Given two numbers, print the greater number.
# i=5
# j=8
# if i>j:
#     print(i)
# else:
#     print(j)  

#6. Given three numbers, print the largest number.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("The largest number is:", a)
# elif b >= a and b >= c:
#     print("The largest number is:", b)
# else:
#     print("The largest number is:", c)

#7. Check whether a year is a leap year.
# y = int(input("Enter a year:"))
# if (y % 4 == 0 and y % 100 != 0):
#  if (y % 400 == 0):
#   print("leap year")
# else:
#  print("not a leap year")

#8. Given a mark, print:
# "Pass" if marks ≥ 40
# "Fail" otherwise
# marks = int(input("Enter the marks: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

#9. Given a mark, print grades:
# A → ≥ 90
# B → ≥ 75
# C → ≥ 60
# Fail → below 60
# marks = int(input("Enter the marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# else:
#     print("Fail")

#10. Check if a character is a vowel or consonant.
# character="c"
# vowels=['a', 'e', 'i', 'o', 'u'] 
# if character in vowels:
#     print(character," is a vowels")
# else:
#     print(character," is a consonent")    

#11. Print numbers from 1 to 10 but stop when number is 6.  
# i=1
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)  

#12. Print numbers from 1 to 10 but skip number 5.
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

#13.Use pass inside an if block and explain why it doesn’t cause an error.  
# i=1
# if i>5:
#     pass
# else:
#     print("The pass statementn in python is a null operation; it does nothing and act as a") 

#14. Print all even numbers between 1 and 20 .
# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num)

#15. Find the sum of numbers from 1 to 10.
# sum=0
# for i in range(1,11):
#      sum+=i
# print(sum)      

#16. Check whether a given number is a multiple of both 3 and 5.
# num=int(input("Enter the number:\t"))
# if num%3==0 and num%5==0:
#     print(num,"is multiple of both 3 and 5")
# else:
#     print(num, "is not the multiple of both 3 and 5")    

#17. Print "Hello" 5 times using a loop
# i=1
# while i<=5:
#     print("Hello")
#     i+=1

#18. Given a list [1,2,3,4,5] , print only numbers greater than 3.
# list1=[1,2,3,4,5]
# i=1
# for i in list1:
#     if i>3:
#         print(i)

#19. Advanced Login System
# Write a Python program to simulate a login system with the following rules:
# The correct username is "admin" and the correct password is "1234" .
# The user is allowed a maximum of 3 login attempts.
# The username comparison should be case-insensitive.
# The password comparison should be case-sensitive.
# If the user enters correct credentials within the allowed attempts, display
# Login successful .
# If all attempts are used without success, display
# Account locked .
# After each failed attempt, display the number of attempts remaining.
# correct_username = "admin"
# correct_password = "1234"
# max_attempts = 3
# for attempts in range(1,max_attempts+1):
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username.lower() == correct_username and password == correct_password:
#             print("Login successful")
#             break
#     else:
#              remaining_attempts-= 1  
#              if remaining_attempts> 0:
#                 print(f"incorrect credentials.Attempts remaining:{remaining_attempts}")
#              else:
#                 print("Account locked")


#20. Enhanced Traffic Light Controller
# Write a Python program that acts as a traffic light controller with the following
# conditions:
# The program should accept either a color or a number as input.
# Use the mapping:
# 1 or "red" → Stop and wait for 60 seconds
# 2 or "yellow" → Ready and wait for 5 seconds
# 3 or "green" → Go and drive safely
# The program should handle inputs in a case-insensitive manner.
# If the input does not match any valid color or number, display
# Invalid signal .
# siginal = input("Enter traffic light signal (color or number):")
# siginal=siginal.lower()    
# if siginal == "red" or siginal== "1":
#         print("Stop and wait for 60 seconds.") 
# elif siginal == "yellow" or siginal == "2":
#         print("Ready and wait for 5 seconds.")
# elif siginal == "green" or siginal == "3":
#         print("Go and drive safely.")
# else:
#         print("Invalid signal.")

#LIST COMPREHENSION QUESTIONS

#1. Given a list of numbers, write a program to find the sum of all numbers, the
# sum of even numbers, and the sum of odd numbers using list
# comprehension
# Given list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Sum of all numbers
# sum_all = sum([num for num in numbers])

# # Sum of even numbers
# sum_even = sum([num for num in numbers if num % 2 == 0])

# # Sum of odd numbers
# sum_odd = sum([num for num in numbers if num % 2 != 0])

# # Display results
# print("Sum of all numbers:", sum_all)
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)

#2. Given a list of numbers, create a new list that contains only numbers
# # greater than 10 and divisible by 3 using list comprehension.
# # Given list of numbers
# numbers = [3, 6, 9, 12, 15, 18, 21, 25, 30, 4, 7, 10]

# # List comprehension to filter numbers
# result = [num for num in numbers if num > 10 and num % 3 == 0]

# # Display result
# print("Numbers greater than 10 and divisible by 3:", result)

# 3. Given a list of numbers, create a new list containing only even numbers
# greater than 10 using list comprehension.
# Given list of numbers
# numbers = [2, 5, 8, 10, 12, 14, 17, 20, 22, 25, 30]

# # List comprehension to filter even numbers greater than 10
# even_greater_than_10 = [num for num in numbers if num > 10 and num % 2 == 0]

# # Display result
# print("Even numbers greater than 10:", even_greater_than_10)

#4. Given a list of strings, create a new list containing the length of each string
# using list comprehension.
# Given list of strings
# strings = ["apple", "banana", "cherry", "date", "fig"]

# # List comprehension to get lengths of strings
# lengths = [len(s) for s in strings]

# # Display result
# print("Lengths of each string:", lengths)

#5. Given a list of numbers, create a new list where:
# even numbers are replaced with "even"
# odd numbers are replaced with "odd"
# Given list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = ["even" if num % 2 == 0 else "odd" for num in numbers]
# print("Replaced list:", result)





        

    



       


    

 

