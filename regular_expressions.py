# # 1. re.search(pattern, string)
# import re
# text = "Hello world"
# print(re.search(r"world", text))

# # 2. re.match(pattern, string)
# text = "Hello world"
# print(re.match(r"Hello", text))
# print(re.match(r"world", text))

# # 3. re.findall(pattern, string)
# text = "I have 2 apples and 5 oranges."
# print(re.findall(r"\d+", text))
# text = "The price is 45 dollars, 30 cents, and 50 rupees."
# print(re.findall(r"\d+", text))

# # 4. re.finditer(pattern, string)
# text = "I have 2 apples and 5 oranges."
# for match in re.finditer(r"\d+", text):
#  print(match.group(), "at", match.start())

# # 5. re.sub(pattern, repl, string)
# text = "Hello 123, welcome 456!"
# print(re.sub(r"\d+", "number", text))

# # 6. re.split(pattern, string)
# text = "apple, orange; banana, grape"
# print(re.split(r"[;,]", text))

# # 7. Grouping & Capturing
# text = "John: 34, Alice: 45, Bob: 23"
# print(re.findall(r"(\w+): (\d+)", text))

# # 11.Compiling Regex
# pattern = re.compile(r"\d+")
# text = "123 apples and 456 oranges"
# print(pattern.findall(text)) 

# 12. Regex Flags
# 1. re.IGNORECASE (or re.I )
# import re
# text = "HELLO world"
# print(re.search(r"hello", text, re.IGNORECASE))

# # 2. re.MULTILINE (or re.M )
# text = """first line
# second line
# third line"""
# # Find all lines starting with 's'
# print(re.findall(r"^s\w+", text, re.MULTILINE))
# # ['second']
# # Find all lines ending with 'e'
# print(re.findall(r"\w+e$", text, re.MULTILINE)) 

# # 3. re.DOTALL (or re.S )
# text = "Hello\nWorld"
# # Normal dot (.) → won't cross newline
# print(re.search(r"Hello.*World", text))
# print(re.search(r"Hello.*World", text, re.DOTALL))

# Real-Life Uses of Regular Expressions
# 1. Validation (Checking Input)
import re
email = "user@example.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
 print("Valid email")
else:
 print("Invalid email")

#  2. Data Cleaning
text = "Price: $123.45"
print(re.sub(r"[^0-9.]", "", text))

# 3. Text Extraction
tweet = "Excited for #Python3 and following @openai!"
print(re.findall(r"#\w+", tweet)) 
print(re.findall(r"@\w+", tweet)) 

# 4. Search & Replace
text = "Card: 1234-5678-9012-3456"
print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", text))





