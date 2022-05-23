# Classes Objects and Recursion
> reading assignment 04

## Why this topic matters
This topic matters because OOP(object oriented programming) is a driving force behind good coding practices. Being able to create a class template that creates objects allows easy storage of data with similar input, allows better ways to access information rather than just creating variables everytime with inputs and more. 

there are so many benefits to using objects over creating unique variables for everything. Classes make it extremely easy to create the objects I need without needed to make a new object every time from scratch. 


### Classes
classes are a way to create objects. They would be described as a template for creating objects. 

The dot notation is used to access the properties and values from an object.

                 -Example- 
    class Example: 
        name = 'Brendon'
        height = '6'1'
        weight = 205
    
    newExample = Example()
    print(newExample.name) 

                -Result-
                 Brendon
to access a function of an class object, you would do the same as accessing a variable however, you need the function parenth's to invoke the function. 

### Recursion
- a recursive function is a function that calls itself until a condition is met. It is very important that a condition can be resolved or the function will become a inifinite loop and that is bad!.
- a way to think about using recursion is to make it in a way that everytime a function calls itself it breaks the problem down into further chunks, solving smaller pieces at a time. This is compared to solving the problem iteratively.
- a good example or recursion at work is the fibbonacci sequence. You set the starting nums to 0 and 1, then run the function recursivly using the value passed. The function will run getting smaller and smaller on the call stack and return the result once the condition is met. Just be careful with how big a number you use for the value passed into the function. 

## Things I want to know more about

I would like to know more about the self argument, it looks like it is used to pull the properties of its own object created. I wonder if you can pull the values of other objects by instantiating the current object with the function as part of a local function.  