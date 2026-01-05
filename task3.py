odd=[]
even=[]
for i in range(1,11):
    if i%2==0:
     even.append(i)  
    else:
     odd.append(i)
print("odd numbers :",odd)
print("even numbers :",even)    

a=[x**2 for x in range(1,11)]
print(a)
