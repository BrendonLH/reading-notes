# Class 401-Javascript Reading Notes

## React Native

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

    1. Compare and Contrast Redux Toolkit with Redux “Ducks”
        a. Ducks is a modular pattern that collocates actions, action types and reducers into a single file.

        b. React redux toolkit typically has you split your actions and reducers up into seperate files. 

    2. What is the principle advantage of Redux Toolkit
        a. Being able to easily configure A redux store and simplifying the boilerplate.
    

### Vocabulary Terms

**redux toolkit slices:** 
    - takes an object of reducer functions, a slice name, and an initial state value and lets us auto-generate action types and action creators, based on the names of the reducer functions that we supply.
**namespace:**
    - namespaces allow us to prevent collisions and crashes between variables and functions. This is a way to uniquely identify something that can have the same context as others, examples would be objects having the same properties but the namespace is different.

    Car = {
        start: true
    } 

    turkey = {
        start: false
    } 

    Car.start = true
    turkey.start = false


