# Class 401-Javascript Reading Notes

## API-server

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. How does route prefixing work with an external routing module?
    - a. use let router = express.Router() in order to create the router prefix. Using the prefixing allows better modularization for multiple routes in different files. 

2. When routing, what’s the difference between app.get('/data/:id') and app.get('/data/:name')?

    - getting the ID will get the ID from the object. The name will get the Name from the object.

3. Explain how Express handles routing conflicts?
    - It gives you a 404 error


4. What are the ways that a browser can send “data” or request variables to an HTTP server?
    - GET
    - POST
    - PUT

### Vocabulary Terms

**Routing:** 
    - refers to how an application’s endpoints (URIs) respond to client requests.

**Route Prefixing:**
    - used to set a common prefix for an entire controller.

**Request "Body":** 
    - data sent by the client to your API.
    
**Request "Query":** 
    - the query string sent to the server

**Request "Params:**
    -  returns parameters in the matched route.
