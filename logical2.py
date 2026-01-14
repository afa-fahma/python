# 1.Valid Parentheses
# You are given a string containing only ( and ). Determine whether the string is balanced. Example Inputs and Outputs:
# Input: "((()))" Output: True
# Input: "(()" Output: False
n=(input("Enter a string:"))
count=0
for i in n:
    if i =="(":
        count+=1
    else:
        count -=1
    if count<0:
        print("false")
        break
else:
    if count==0:
        print("true") 
    else:
        print("false")
       
       
# 2.Longest Word
# You are given a sentence. Find the longest word in the sentence. If multiple words havethesame length, return the first one. Example Inputs and Outputs:
# Input: "Python programming is very powerful" Output: "programming"

# sentence=input("Enter a sentence:").split()
# longest=""
# for i in sentence:
#     if len(i)>len(longest):
#        longest=i
# print(f"longest word:{longest}")      
 
 