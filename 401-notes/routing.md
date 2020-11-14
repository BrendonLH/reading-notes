# Class 401-Javascript Reading Notes

## Routing

## Table of Contents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Do child components have direct access to props/state from the parent?
    - Yes and no, You have to pass down the props/state in the parent.
2. When a component “wraps” another component, how does the child component’s output get rendered?
    - Its gets rendered using the this.props.children because the wrapped componenent is now a child of the wrapper.
3. Can a component, such as <Content />, which is a child also be used as a standalone component elsewhere in the application?
    - Yes components can be used again
4. What trick can a parent use to share all props with it’s children
    - a parent can pass all of its state as props. 

    

### Vocabulary Terms

**props.children:** 
    - Any component that has child components as sub components

**composition:**
    - Allows You to make more functionality by combining functions such as map and filter together.


