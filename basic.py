# a=10
# print(type(a))

# a=10
# b="afafahma"
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# r=True
# s=False
# print(type(r))
# print(type(s))


# s=[1,2,3,4]
# print(s)
# r=["apple","orange","grape"]
# print(r)

# s={"apple","orange","grapes","guava","apple","kiwi"}  #set no order no repeat
# print(s)

# s={
#     "name":"afafahma",
#     "name2":"afafahma",
#     "age":20,
#     "place":"kalikavu"
# }
# print(s)
# s=3.55
# r=122222
# t=4655.3545
# u=10+10j
# print(type(s))
# print(type(r))
# print(type(t))
# print(type(u))

# a=print("hiii")
# print(b)

# n= int(input("number:"))
# print(n)

# file =open("files.txt","r")
# print(file.read())

# a= 10
# b= "5"
# print(a+b)

# try:
#  file = open("filess.txt", "r")
#  content = file.read()
# except FileNotFoundError:
#  print("File not found!")
# finally:
#  file.close()

# x=-5
# if x<0:
#     raise Exception("negative numbers not allowed")

class NegativeNumberError(Exception):
 pass
def check_number(num):
  if num < 0:
   raise NegativeNumberError("Negative numbers are notallowed!")
try:
 check_number(-10)
except NegativeNumberError as e:
 print(e)
