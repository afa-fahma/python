# 1.Reverse Words in a Sentence
# You are given a sentence. Reverse each word individually while keeping the word order thesame. Example Inputs and Outputs:
# Input: "Hello World" Output: "olleH dlroW"
# Input: "Python is fun" Output: "nohtyP si nuf" 
# sentence=input("Enter the sentance:")
# words=sentence.split()
# for i in range(len(words)):
#     words[i]=words[i][::-1]
# print(" ".join(words))    
    

# 2.Longest Common Prefix
# You are given a list of strings. Find the longest common prefix among them. Example Inputs and Outputs:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Input: ["dog","racecar","car"]
# Output: ""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

print(longestCommonPrefix(["flower","flow","flight"])) 
print(longestCommonPrefix(["dog","racecar","car"])) 
