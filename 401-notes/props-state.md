# Class 401-Javascript Reading Notes

## Props and State

## Table of Contents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Does a deployed React application require a server?
    - No
2. Why do we prefer to test a React application at the behavior rather than the unit level?
    -  Testing using implementation details can result in false positives and false negatives.
3. What does npm run build do?
    -  runs the script "build" and created a script which runs your application 
4. Describe the actual composition / architecture of a React application
    - React is made up of components. The components do not directly interact with each other but instead change the data and then pass it back up and out using the setState at the parent level. Components are children of the application and silblings of each other.

### Vocabulary Terms

**BDD**
    - Behaviour-Driven Development (BDD) is a collaborative approach to software development that bridges the communication gap between business and IT
**Acceptance Tests**
    - Formal testing with respect to user needs, requirements, and business processes conducted to determine whether or not a system satisfies the acceptance criteria and to enable the user, customers or other authorized entity to determine whether or not to accept the system.
**mounting**
    - the process of outputting the virtual representation of a component into the final UI representation (e.g. DOM or Native Components).
**build**
    - the plumbing command called by npm link and npm install.
