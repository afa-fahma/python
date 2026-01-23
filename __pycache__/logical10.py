# 1. Bank Management Logic (Menu-Driven Program)
# Problem Statement:
# Create a simple Bank Management System using your preferred
# programming language.
# Requirements:
# 1. Start with an initial balance (e.g., ₹1000)
# 2. Display a menu repeatedly until the user exits:
# ○ 1. Check Balance
# ○ 2. Deposit
# ○ 3. Withdraw
# ○ 4. Exit
# 3. Implement the following logic:
# ○ Check Balance: Display current balance
# ○ Deposit: Add entered amount to balance (amount > 0)
# ○ Withdraw:
# ■ Amount should be > 0
# ■ Amount should not exceed current balance
# ■ Display error if insufficient balance
# ○ Exit: Stop the program
# Constraints:
# ● Balance must never be negative
# ● Handle invalid menu choices gracefully
# 👉 This tests loops(while), conditionals, and user input handling.
# balance=float(input("Enter initial balance:"))

# while True:
#     print("\n1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         print("Balance:", balance)

#     elif choice == 2:
#         amount = int(input("Enter amount: "))
#         if amount > 0:
#             balance = balance + amount
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         amount = int(input("Enter amount: "))
#         if amount > 0 and amount <= balance:
#             balance = balance - amount
#         else:
#             print("Error")


#     elif choice == 4:
#         print("Exit")
#         break

#     else:
#         print("Invalid choice")

# 2. Pattern Printing – Butterfly Pattern (Medium
# Level)
# Problem Statement:
# Write a program to print a butterfly pattern of size N.
# Input: N = 4
# Rules:
# ● First half prints increasing stars
# ● Middle has full stars
# ● Second half mirrors the first half
# 👉 This tests nested loops, symmetry, and spacing logic.
# n = 4
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)

# for i in range(n, 0, -1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)


# number=int(input("Enter the number:"))

# reverse = 0

# while number > 0:
#     digit = number % 10      
#     reverse = reverse * 10 + digit
#     number = number // 10    

# print("Reversed Number =", reverse)