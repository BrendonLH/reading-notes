# Class 401-Javascript Reading Notes

## Event Driven Applications

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Why is access control important?
    - Access control keeps only the desired users able to access an application. This helps prevent malicious intent from unauthorized users.
2. Describe an application that would need access control.
    - Youtube, Slack, oher apps that require a user to access there own information but cant access or change other users infomation. I cant go into the other 401 slack channel and change things for instance. 
3. What is a role used for?
    - Allows an application to assign permissions that grants access.
4. Why is role based access control more scalable than discretionary or mandatory access control?
    - Mandatory Access Control requires a considerable amount of planning before it can be effectively implemented. Once implemented it also imposes a high system management overhead due to the need to constantly update object and account labels to accommodate new data, new users and changes in the categorization and classification of existing users.
    - under Discretionary action control a user can only set access permissions for resources which they already own.
    - Role based allows new users to easily be assigned a role that does not change permissions depending on the user, in example, a user assigned a role of basic will have the same exact permissions as a different user assigned with the same role. One persons role cannot be given different permissions without changing their role. it will be the same as other users with that same role.  
    

### Vocabulary Terms

**Authorization:** 
    - used to determine user/client privileges or access levels related to system resources.
**Role Based Access Control:**
    - RBAC is based on a user's job function within the organization to which the computer system belongs.

**Capabilities:** 
    - What a User is allowed to do with the permissions granted (CRUD).
    

## Event Driven Notes

1. Events are things that are triggered when A button is clicked, someone signs up, Joins a chat or an event can even be triggered when a user logs out. 