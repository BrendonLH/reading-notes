# Class 401-Javascript Reading Notes

## Functional Programming

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Name 3 advantages to Test Driven Development
    - a. Identify The Problem Quickly
    - a. Forces writing of small lasses focused on one thing
    - a. Maintainable, Flexible and easily extendable code
2. In what case would you need to use beforeEach() or afterEach() in a test suite?
    - a. If you have work you need to do repeatedly for many tests
3. What is one downside of Test Driven Development
    - a. uses alot of time and effort up front
4. What’s the primary difference between ES6 Classes and Constructor/Prototype Classes?
    - a. ES6 classes automatically assign the prototype to the object.
5. Name a use case for a static method
    - a. used to create utility functions
6. Write an example of a Higher Order function and describe the use case it solves
    - a. sort would be an higher order function if i pass an argument into it. I can pass in a argument into a sort that could maybe sort from a-b from an array of values.
### Vocabulary Terms

* functional programming
    - a. Functional programming (FP) is a programming paradigm for developing software using functions.
* pure function
    - a. a Deterministic function. Same input equals same output.
* higher-order function
    - a. a function that recieves a function as an argument.
* immutable state
 - a. cannot be changed or modified after it is created.
* object
    - a. variables that contain multiple values.
* object-oriented programming (OOP)
    - a. Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).
* class
    - a. The class declaration creates a new class with a given name using prototype-based inheritance.
* prototype
    - a. Each object has a private property which holds a link to another object called its prototype.
* super
    - a. The super keyword is used to access and call functions on an object's parent.
* inheritance
    - a. the notion that one object's methods/properties are available to be used via another object. 
* constructor
    - a. The constructor property returns a reference to the Object constructor function that created the instance object. 
* instance
    - a. an object that you create out of a constructor function in javascript.
* context
    refers to an object.
* this
    - a. refers to the object it belongs to.
* Test Driven Development (TDD)
    - a. Test-driven development (TDD) is a technique for ensuring that your code does what you think it does
* Jest
    - a. Jest is a JavaScript testing framework designed to ensure correctness of any JavaScript codebase.
* Continuous Integration (CI)
    - a. the practice of merging all developer working copies to a shared mainline several times a day.
* unit test
    - a. Unit tests check blocks of code to ensure that they all run as expected.