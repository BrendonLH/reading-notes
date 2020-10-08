# Class 401-Javascript Reading Notes

## Socket IO

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

What is the benefit of transforming data into packets?
    - Smaller more efficient chunks of data. the alternative would be circuit switching which would need an established connection where as packet switching will still be connected on idle.
UDP is often refereed to as a connectionless protocol. Why is this?
    - UDP does not use handshaking or checking if a device is connected.
Can a socket server application have multiple socket connections?
    - yes, as long as the socket is read somewhere else. 
Can a socket connection application be connected to multiple socket servers?
    - no, only gets one port to socket too.
Can an application be both a socket server and a socket connection?
    - yes, you just need to make sure that your socket isnt listening to its own server. 


    

### Vocabulary Terms

**OSI Model:** 
    - a conceptual model that characterises and standardises the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology.

**TCP Model:**
    - Protocol oriented standard that follows a horizantal approach.

**TCP:** 
    - a communication protocol that establishes a connection with another computer and ensures that the packets are sent and received successfully.
    
**UDP:** 
    - connectionless protocol. When you a send a data or message, you don’t know if it’ll get there, it could get lost on the way

**Packets:**
    - a unit of data made into a single package that travels along a given network path.
**Socket:**
    - a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network.


