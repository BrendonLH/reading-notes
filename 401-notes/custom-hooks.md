# Class 401-Javascript Reading Notes

## Custom Hooks

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions
1. What does a component’s lifecycle refer to?
     - Mounting, Updating, Unmounting
2. Why do you sometimes need to “wrap” functions in useCallback when called from within useEffect
    - so only the function that has made any changes gets re-rendered. 
3. Why are functional components preferred over class components?
     - functoinal components are easier to read and is also can be more easily reused.
4. What is wrong with the following code?

        import React, {useState, useEffect} from 'react';

        function MyComponent(props) {
        const [count, setCount] = useState(0);

        function changeCount(e) {
            setCount(e.target.value);
        }

        let renderedItems = []

        for (let i = 0; i < count; i++) {
            useEffect( () => {
            console.log('component mount/update');
            }, [count]);

            renderedItems.push(<div key={i}>Item</div>);
        }

        return (<div>
            <input type='number' value={count} onChange={changeCount}/>
            {renderedItems}
            </div>);
        }

    - When I put this in and try to run it, I get "rendered more hooks than during the previous render". from the reading, one of the rules it says never call a hook from inside a loop. Im assuming that means that our useEffect is causing the issue because it is inside a for loop.

    

### Vocabulary Terms

**State Hook:** 
    - useState() hook allows one to declare a state variable inside a function.

**Effect Hook:**
    - The Effect Hook lets you perform side effects in function components.

**Reducer Hook:** 
    - takes three arguments including reducer, initial state, and the function to load the initial state lazily.
    
**React Hook-Async:** 
    - When we are using async in react we must also make a new variable that useAsyncHook().

**:**
    -

**:**
    -

**:**
    -

**:**
    - 

