# Class 401-Javascript Reading Notes

## Express Routing & Connected API

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Name 3 real world use cases where you’d want to change the request with custom middleware?
    - a. We can use middleware to inject errors and status codes before it has to go out and travel all the way back
    - a. We Can use Middleware to make timestamp logs. 
    - a. We can use middleware to translate a json file.

2. True or false: The route handler is middleware?
    - a. True

3. In what ways can a middleware function end the process and send data to the browser?
    - a. 

4. At what point in the request lifecycle can you “inject” middleware?
    - a. after the request has been made and before the response. 

5. What can cause express to error with “Request headers sent twice, cannot start a second response”?
    - a. when the headers have already been sent and your code is trying to send them again so they cant be set again.

    

### Vocabulary Terms

**Middleware:** 

        - software that acts as a bridge between an operating system or database and applications, especially on a network.

**Request Object:**

        - The Request object retrieves the values that the client browser passed to the server during an HTTP request. 

**Response Object:**

        - The res object represents the HTTP response that an Express app sends when it gets an HTTP request.
    
**Appplication Middleware:** 

        - 

**Routing Middleware:**

        -  The routing has been implemented as middleware.

