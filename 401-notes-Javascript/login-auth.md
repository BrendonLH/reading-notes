# Class 401-Javascript Reading Notes

## Login and Auth

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions


1. Why is the Context API useful?
    - It allows us to share state across the entire application
2. Can a component outside of a provider get its context?
    - no, if the componenet was wrapped inside the provider then yes it could but if not then it has no way on knowing the state.
3. What are some common use cases for using the Context API?
    - When we dont need direct relationships. Broader relationship scopes.
4. Describe “Context Hell”
    - Lots and lots of components. 
    

### Vocabulary Terms

**Global State:** 
    - The state that can be shared between all components. 
**Global Context:**
    - allows data to be used by many different components.

**Provider:** 
    - the container for all React Spectrum applications.
    
**Consumer:** 
    - a component that consumes and uses the state.


