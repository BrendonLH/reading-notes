# Class 401-Javascript Reading Notes

## Context-api

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Describe use cases for useMemo() and useReducer()?
    - useReducer is best used with a complex object, where individual properties need to be worked on.
    - UseMemo memoizes a value and not function, We can use this to save data using cache and only rerender if the data has changed.
2. Why do custom hooks need the use prefix?
    - adding 'use' will allow us to know what is built in and what is a custom hook.
3. What do custom hooks usually do?
    - extract logic from components into reusable functions. 
4. Using any list of custom hooks, research and name one that you think will be useful in your applications
     - https://www.npmjs.com/package/react-hook-form
     - looks like an easy way to build form validation.
5. Describe how a hook that fetches API data might work.
    - you can use useEffect() with async.


    

### Vocabulary Terms

**Reducer:** 
    - a function which takes two arguments -- the current state and an action -- and returns based on both arguments a new state.


