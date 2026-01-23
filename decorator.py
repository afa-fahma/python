# def aaa(func):
#     # """Decorator that adds a print message before and after the wrapped function"""

#     def wrapper():
#         print("hello")
#         func()
#         print("Bye")
#     return wrapper
# @aaa
# def say_name():
#     print("john")
# say_name()   


def decor(func):
    def wrapper(*args,**kwargs):
        print("additon of 2 numbers")
        a=func(*args,**kwargs)
        print(a)
        print("addition done")
    return wrapper   

@decor
def add(a,b):
        return a+b        
add(2,3)

@decor
def sub(a,b):
     return a-b
sub(5,3)


