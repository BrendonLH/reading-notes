# Class 401-Javascript Reading Notes

## Authentication

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Explain what a “Singleton” is (in Computer Science terms)?
    - a. design pattern in which a class ensures that only one instance of it is ever present in memory. 

2. Explain how the Singleton pattern can be used with Node modules, specifically with classes?
    - a. we can use Object.freeze(singletonInstance). We can use singletons to make sure that a referenace to a variable is not redeclared.

3. If you were tasked with building a middleware system like Express uses, what approach might you take to construct/operate it?
    - a. Im not really sure how express works with the PORT, but I think the whole app is built on middleware so I would start by building all the middleware I need. Other than that, All i see is code on how to use express. Not alot on how its actually built. 

### Vocabulary

- Router Middleware
    - Router-level middleware works in the same way as application-level middleware, except it is bound to an instance of express.Router()
- Dynamic Module Loading
    - Loading modules asynchrously rather than statically
- Singelton Pattern
    - the singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance. 
- CRUD -> REST Method Matches
    - Create -> PUT & POST
    - Read -> GET
    - Update -> PUT
    - Delete -> DELETE
- Mock Testing
    - Mock testing is an approach to unit testing that lets you make assertions about how the code under test is interacting with other system modules.

