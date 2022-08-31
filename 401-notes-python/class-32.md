# Readings (class-32)

## Topic : Permissions and PostgreSQL

### DRF Permissions
- Permissions are how we can dictate user interaction with an application. We can set certain parts of an application behind authentication in order to restrict access. 
- (key Terms)
    - Permission
        - used to determine how a User is allowed to interact with an application and what parts.
    - isAuthenticated
        - Simple way to check if a user is allowed to access or is not allowed. 
    - isAuthenticatedOrReadOnly
        - Checks if the user was authenticated or if not authenitcated
        - Allows authenticated users to have more accessability than non-authenticated, non users are considered read only and dont have any crud access. 


## Things I want to Know more about
- Im interested in knowing more about how to restrict access using login from a standalone front end. Like logging in from a separate site, but being able to use isAuthenticated for the backend to determine that the user from the front end is still logged in and able to do things. 

- For instance, is it similar to tokens, where when I log in maybe the front end user is granted a temporary token that is used to make sure the user is still authenticated as they traverse the site? or is there something that django uses specifically to make sure the user is logged in when they are making multiple requests? 