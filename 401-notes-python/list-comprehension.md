# Readings: Ten Thousand 3

### List Comprehension
- list methods allow us to manage lists more elegently and readable
- list methods create more compact code for lists
- list methods are generally faster and more flexible than loops

- range method
  - cleaner than a for loop
  - less code overall

with list methods, you can multiply, each item simply, get the location even set conditionals in the same line. 

----example----
list = [num for num in range(6)]

-----result-----
[0,1,2,3,4,5]

----example2----
list_add_one = [num+1 for num in range(6)]

-----result-----
[1,2,3,4,5,6]


other than numbers we can read a file and then parse it out using list methods as well. There are so many different things we can do with list methods. 

after reading the article, I can see the power of using list comprehension over just writing a for loop for lists. its more compact, readable and takes up less space. 

## Things I want to know more about

is there comprehension methods that pertain to others like dictionary's or tuples? or is it because of mutability vs immutablity?