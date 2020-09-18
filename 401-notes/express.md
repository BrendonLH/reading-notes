# Class 401-Javascript Reading Notes

## Express

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. What’s the difference between PUT and PATCH?
 - a. PUT applies the update to the entire resource where Patch only applies to a part of the rsource

2. Provide links to 3 services or tools that allow you to “mock” an API for development like json-server.
 - a. [Swagger](https://swagger.io/)
 - a. [Mockable](https://mockable.io/)
 - a. [Mock Service Worker](https://mswjs.io/)

3. Compare and contrast Swagger and APIDoc.js. Which HTTP status codes should be sent with each type of (un)successful API call?
 - a. Swagger
    - "200" - ok.
    - "400" - Bad request User ID must be an integer and larger than 0.
    - "401" information is missing or invalid.  
    - "404" A user with the specified ID was not found.
    - "5XX" Unexpected Error.
- a. APIDoc.js
    - 


4. Compare and contrast SOAP and ReST
 - a.  SOAP uses built in protocols and ReST does not. SOAP's built in protocols 
 - a. SOAP is a protocol and ReST is an architectural pattern.  


### Vocabulary Terms

**SOAP:** 
        - SIMple OBJECT ACCESS PROTOCOL. SOAP relies on XML to provide messaging services. SOAP has built in error handling. It is a mesaaging protocol for exchanging information among computers.

**ReST Verbs:**
        - POST, GET, PUT, PATCH and DELETE

**CRUD Verbs:** 
    - CREATE, READ, UPDATE and DESTROY
    
**Swagger:** 
    - Swagger allows you to describe the structure of your APIs so that machines can read them.
