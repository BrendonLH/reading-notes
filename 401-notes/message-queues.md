# Class 401-Javascript Reading Notes

## Message Queues

## Table of Contents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. What does it mean that web sockets are bidirectional? Why is this useful?
    - Both parties can send and recieve data. This is useful because it allows data to not have to always for a response, chat features as an example.  
2. Does socket.io use HTTP? Why?
    - yes, so it can serve its own client code through /socket.io/socket.io.js
3. What happens when a client emits an event?
    - The host recieves the event if its listening for it and then emits a response to any clients listening.
4. What happens when a server emits an event?
    - clients listening for the event recieve it then respond back if thats its job. it could just recieve the response such as a direct chat feature. 
5. What happens if a client “misses” an event?
    - im assuming this means like the event is not passed to the client and nothing happends. 
6. How can we mitigate this?
    - We can put in console.error in the server if its expecting a respoonse or error log on the client side. I think it is better to do it on the host side as i dont know what data im getting back until i get it so if im not recieveing anything then I need to know that. 

    

### Vocabulary Terms

**Web Socket:** 
    - comm protocol allowing for full duplex communication over TCP connection. 
**Socket.io:**
    - a library that enables real-time, bidirectional and event-based communication between the browser and the server.

**Client:** 
    - connects to the server and emits events or responds to events. 
    
**Server:** 
    - How all the clients connect to other events.
