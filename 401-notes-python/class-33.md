# Readings (class-33)

## Topic : Authentication and Production

### Json Web Tokens
- Json Web tokens are a way to use authentication using signatures or pass information securely. This allows better secrurity and authenticity. These can be setup to be public or secret.
- (key Terms)
    - JWT
        - A Json object that represents a header, a payload and signature.
    - Header
        - Contains the type of token as well as the signature algorithm.
    - Payload
        - Information and additional data about the user.
    - Signature
      - the signature is what is used after the encoding. The signature is used to make sure nothing was changed in between sending and recieiving.
- (additional notes)

### Article 2
- (summary of article)
- (key Terms)
    - term 1
        - definition
    - term 2
        - definition
    - term 3
        - definition
- (additional notes)
  - we can use tokens to make sure a user is autenticated/authorized when they try to access secure parts of an application.

### Django Runserver is Not Your Production Server
- (summary of article)
  - The runserver in django command is not a production server command. It is used strictly for development. It is slow and has alot of security flaws.
- (key Terms)
    - Nginx
        - A web server that handles static files
    -  WSGI/Gunicorn
        - The application server that constructs the python objects.
- (additional notes)
  - Nginx and Gunicorn are essential for production if using a host other than heroku. 

## Things I want to Know more about
- (pertains to whole topic of reading)
  - Im interested about Nginx and Gunicorn. I dont quite understand what they are doing. I see alot of tutrials with django requiring these early on in setup, so im wondering if I should set these up prematurely so I can have production ready apps. It is how I build out my react/Node apps. I first make sure it is hosted and running, then I Start making changes and commits.
  - Im wondering if I should be building my django apps very similarly. 