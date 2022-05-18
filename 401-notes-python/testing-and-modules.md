# Testing and Modules

## In Tests We Trust — TDD with Python
>by Ana Paula Gomes

### AAA
for the first section of the reading, I didnt understand some of the key terms the author was using and after doing some extensive research I was able to understand that the first section was talking about setting up tests so that they can be a living and changing documentation.

you're tests should be setup in a way that can still be applied as the application grows and matures. Tests should reflect the lifespan of the application.

The second section talks about the fundamentals of unit testing (AAA). From my understanding....
* ARRANGE - Gather what variables you need, Object creation. Gathering the Data.
* ACT - This is when we actually envoke our code using a testing method. 
* ASSERT - This is the step where we actually check if our test returns a value and that value is what is expected.

### TDD cycle
 this section talks about The TDD Cycle. The **TDD cycle** seemed pretty straightforward. 
 * The first test you make should be a failing test. there is nothing yet to actually test so it should fail. 
 * The second test should be a passing test representing you are in fact getting the result desired. 
 * After the tests is the refactoring process.  

 ## If name equals main

 I am still confused by how main and modules work toegther, from what I gather so far...

 ``` if __name__ = __main__: ``` - this would be the main gate file. if pythons interpretor is running this file, then the name would be ```__main__```
 >if this is file is being imported from another module, the ```__name__``` will be set to whatever that modules name is. 

 ## Recursion
* _The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function._

a recursive function is a function that calls itself if a certain condition is not met. Once the condition is met, the function ends.