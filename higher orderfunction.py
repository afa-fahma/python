def calculate(a,b,operations):
    return operations(a,b)
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print(calculate(10,20,mul))
print(calculate(10,20,div))
print(calculate(10,20,sub))
print(calculate(10,20,add))
