# Class 401-Javascript Reading Notes

## TCP-Servers

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions
1. Given the examples of front-end events such as button click, window resize, form submit, etc, what are some examples of back-end events?
    - Bearer Auth, When a user tries to access a restricted route, an event is triggered to check if the user has permissions.
2. Why are events sometimes better than asynchronous actions with callbacks?
    - callbacks describe something that is happenening where events are something that already happened. 
3. What does an EventEmitter instance do?
    - used to register listeners, every function attached to the event are called synchronously. 
4. When is a program’s call stack, event queue, and event loop active?
    - call stack is executed first one by one unless its asynchronous, then moves to the Queue ( asynchronous code), after word back to the event loop that continuously runs and checks the main stack.
5. What is TCP? 
    - Reliable connections-oriented transfer prototcol


    

### Vocabulary Terms

**Observer Pattern:** 
    - software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

**Listener:**
    -  react to events, but not signal back to their subjects, so the Listener pattern seems a less general case of an Observer.

**Event Handler:** 
    - a callback routine that operates asynchronously and handles inputs received into a program (events).
    
**Event Driven Programming:** 
    - programming paradigm in which the flow of the program is determined by events such as user actions (mouse clicks, key presses), sensor outputs, or messages from other programs or threads.

**Event Loop:**
    - continuously routes incoming events to objects for handling and, as a result of that handling, updates its appearance and state. 

**Event Queue:**
    -   An Event Queue is a data structure storing the list of events using the FIFO(First In First Out) policy.

**Call Stack:**
    - Utilized LIFO to determine how functions and data is processed. 

**Emit/Raise/Trigger:**
    - emit() is used to fire events
    - Triggers signal that an action was completed.
**Subscribe:**
    -

**Database:**
    - an organized collection of data, generally stored and accessed electronically from a computer system.

