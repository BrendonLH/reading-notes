# Class 401-Javascript Reading Notes

## Bearer Authorization

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions
    1. Write the following steps in the correct order:
        * Register your application to get a client_id and client_secret
        * Receive authorization code
        * Ask the client if they want to sign in via a third party
        * Make a request to a third-party API endpoint
        * Redirect to a third party authentication endpoint
        * Make a request to the access token endpoint
        * Receive access token

    2. What can you do with an authorization code?
        a. Access stuff..... looks up granted permissions or consents.

    3. What can you do with an access token?
        a. The user doesnt have to login everytime, the user can just use the token since they have already been verified. 

    4. What’s a benefit of using OAuth instead of your own basic authentication?
        a. OAuth works based on tokens and authorization. 

    

### Vocabulary Terms

**Client ID:** 
    - Public Idententifier for apps
**Client Secret:**
    - a secret only known to the application and authorization server

**Athentication Endpoint:** 
    - Endpoint authentication is an authentication mechanism used to verify the identity of a network's external or remote connecting device.
    
**Access Token Endpoint:** 
    - Lets the client access the requested resource if porper cred is provided.

**API Endpoint:**
    - the point of entry in a communication channel when two systems are interacting.
**Authorization Code:**
    - the code obtained from the authorisation endpoint which the server uses to look up the granted permission or consent.
**Access Token:**
    - contains the security credentials for a login session and identifies the user, the user's groups, the user's privileges, and, in some cases, a particular application. 

1.  Which 3 things had you heard about previously and now have better clarity on?
    1. Token
    2. Authentication
    3. Authorization

2.  Which 3 things are you hoping to learn more about in the upcoming lecture/demo?
    1. How the flow of it all works
    2. Can I use multiple tokens to assign permissions 
    3. Endpoints

3.  What are you most excited about trying to implement or see how it works?
    1. Creating a user login with multiple permissions IE. Admin, User.

