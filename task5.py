# Task 1:Given a positive integer n:
# ● If 1 ≤ n ≤ 9, print its lowercase English word (one to nine).
# ● If n > 9, print Greater than 9.
# Input Format
# ● A single integer n
# Output Format
# ● Print the corresponding word for numbers 1–9, otherwise print Greater than 9.
# Sample Input
# 5
# Sample Output
# five
# n=int(input("enter a number:"))
# list1=['1','2','3','4','5','6','7','8','9']
# list2=["one","two","three","four","five","six","seven","eight","nine"]

# if n>=1 and  n<=9:

#     print(list2[n-1])
# else:
#     print("greater than nine")    

# Task 2:Given a positive integer N, print numbers from 1 to N with the
# following rules:
# ● If the number is divisible by 3, print Fizz
# ● If the number is divisible by 5, print Buzz
# ● If the number is divisible by both 3 and 5, print FizzBuzz
# ● Otherwise, print the number itself
# Input Format
# ● A single integer N
# Output Format
# ● Print the result for each number from 1 to N on a new line

N = int(input("Enter a positive integer:"))

for m in range(1, N + 1):
    if m % 3 == 0 and m % 5 == 0:
        print("FizzBuzz")
    elif m % 3 == 0:
        print("Fizz")
    elif m % 5 == 0:
        print("Buzz")
    else:
        print(m)





   