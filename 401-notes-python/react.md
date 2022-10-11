# Readings (class-37)

## Topic : React 1

### Introducting JSX
- JSX is similar to a tedmplate but it can be fully utilized with javascript. JSX is used to produce React elements.
- (key Terms)
    - JSX
        - (example)
          - let title = <h1>Reading Class 37</h1>;
        - This will render and H1 html when coupling with react.
        - (example)
          - let first = "Brendon";
          - let last = 'Hampton';
          - const firstLast = <div>My name is {first}{last}</div>;
- (additional notes)
  - JSX is a very quick way to add custom elements to be rendered. It allows to make handling logic easier to follow throughout a programs lifecycle.
  - We can use JSX as expressions as well, using it in functions, returning html elements and performing logic.

### Components and Props
- (summary of article)
  - The main takeaway about props is that they are READ ONLY, functions with props should not modify the prop! We can return something else using the props values but we need to keep functions PURE.


## Things I want to Know more about
- (pertains to whole topic of reading)
  - I like React, I do not like props. It gets confusing about having to keep things a Pure function sometimes, thats why I like using Redux for everything. However, I Think props are because the UI needs to not actually modify data, thats what the backend is for im thinking. If thats the case, then the backend doesnt need to worry about props, it just needs request and then can do its magic and return.
  - are props mainly used for the static side of react? 