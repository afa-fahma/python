

#1-Create a tuple (1,2,3,4) and access the element 3 using indexing
my_tuple = (1, 2, 3, 4)
print(my_tuple[2])

#2-Convert the tuple (10,20,30) into a list
my_tuple = (10, 20, 30)
list1 = list(my_tuple)
print(list1)

#3-Convert the list [1,2,3] into a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

#4- From the tuple ("a","b","c","d") , extract ("b","c") using slicing
tuple1 = ("a", "b", "c", "d")
tuple2 = tuple1[1:3]
print(tuple2)

#5- Check if "x" exists inside the tuple ("x","y","z")
a = ("x", "y", "z")
b= "x" in a
print(b)

#6-Given (5,3,9,1) , find the maximum value using a tuple function
t = (5, 3, 9, 1)
u= max(t)
print(u)

#7-Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only
t = (1, 2, 3)
u=(1,2,3)
print(t+u)

#8-Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
t = (1, 2, 2, 3, 2)
u= t.count(2)
print(u)

#9- Find the index of "cat" in ("dog","cat","mouse") .
t = ("dog", "cat", "mouse")
u= t.index("cat")
print(u)

#10-Reverse (1,2,3,4,5) using slicing.
t = (1, 2, 3, 4, 5)
u = t[::-1]
print(u)

#11-Combine (1,2) and (3,4) into (1,2,3,4) using tuple operations
t1 = (1, 2)
t2 = (3, 4)
add= t1 + t2
print(add)

#12-Convert "hello" into a tuple of characters
h = "hello"
i = tuple(h)
print(i)

#13- Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements.
t = (1,2,3,4)
result = [t[0], t[-1]]
print(result)

#14-Given a tuple (10,20,30,40) , replace the value 30 with 99 (hint: convert to list → modify → convert back)
t = (10,20,30,40)
temp_list = list(t)   
temp_list[2] = 99     
t = tuple(temp_list)  
print(t)

#15- Using unpacking, extract a=1 , b=2 , c=3 from (1,2,3) .
t = (1,2,3)
a, b, c = t
print(a, b, c)

#16-Create a nested tuple: turn (1,2,3) into ((1,2,3),) .
t = (1,2,3)
nested = (t,)
print(nested)

#17-Merge ("a","b") with ["c","d"] to get a single tuple ("a","b","c","d") (hint: convert list → tuple).
t1 = ("a", "b")
l = ["c", "d"]
result = t1 + tuple(l)
print(result)

#18-Check if tuple (1,2,3) is equal to its reverse
t = (1,2,3)

result = t == t[::-1]
print(result)

#19- Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4] .
t = ([1,2], [3,4])
result = []

for sublist in t:
    result.extend(sublist)

print(result)

#20-Given (1, [2,3], 4) , add 5 inside the inner list so result becomes (1, [2,3,5], 4) .
t = (1, [2,3], 4)
t[1].append(5)

print(t)

