# FileIO and Exceptions

## Read and Write Files in Python

file are compones of three main parts:
 1. Header - metadata (file name, size, type ect..)
 2. Data - contents of the file
 3. Head of File - special character that indicates the end of file

 file paths are broken into three main parts
 1. folder path - file folder location on the system 
 2. file name - the name of the file
 3. extension - the end of the file path prepending with a (.)

 Python commands
 open an file = __file = open('dog_breeds.txt')__ 
 Read a file = __test = file.read()__

 there are 3 catagories of files
 1. text
 2. buffered
 3. raw


## Exceptions

 a syntax error is different that an exceptions error.
 syntax error - incorrect syntax like not putting a bracket somewhere, the console or the linter can pick this up.
 exceptions error - when your syntax is correct but still get an error, there will be details of the type of error.

 ## try/except block
this is similar to try and catch for javascript only....
this will try a block of code, then either run the block if it has no errors, or returns a exception error.
    
    - try: 
        def func(num):
        num + num = 2
      except:
        print('try 1')

    if you try the function with anything but 1, the except function will run.

## Things I want to know more about

 - can u modify what is returned with an exception error? to make it more readable? 