# Class 401-Javascript Reading Notes

## Advannced Mongo

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions
1. Why would a developer choose to make data models?
    - a. to be able to determine how the structure of the data will be.
2. What purpose do CRUD operations serve?
    - a. Crud allows us to create, read, update and delete. This could be used for if a user needs to create an account, update user info all in relation to the database.
3. What kind of database is Postgres? What kind of database is MongoDB?
    - a. Postgres is a relational database and MongoDB is non-relational.
4. What is Mongoose and why do we need it?
    - a. Mongoose allows us to model application data with built in type casting, query building and validation.
5. Describe how NoSQL Databases scale horizontally
    - a. They scale out rather than up
6. Give one strong argument for and against NoSQL Databases
    - Pro. Easily Felxible when it comes to scaling, Can store massive amounts of data
    - Con. Not mature, less functional, less support due to not being around as long.
7. Define three related pieces of data in a possible application. An example for a store application might be Product, Category and Department. Describe the constraints and rules on each piece of data and how you would relate these pieces to each other. For example, each Product has a Category and belongs in a Department.
    - a. Gaming App
        1. User Profile Name
        2. Profile Saved Game Data
        3. Profile Friends Lists
    - The user makes a profile which is then attached to any games that are played and saved. As a User is playing games and meeting people, they add people to a friends list that is stored specific to them.
8. Name 3 cloud based NoSQL Databases
    - a. Azure
    - a. Amazon web services (AWS)
    - a. MongoDB


### Vocabulary Terms

- database
    - Software that is used to manage data and information structured as fields, records and files.
- data model
    - Data modeling (data modelling) is the process of creating a data model for the data to be stored in a Database. 
- CRUD
    - Create, Read, Update, Delete.
- schema
    - A file used as a blueprint for how data should be formatted inside of a database.
- sanitize
    - In relation to web input forms, sanitizing is when a server handles user input and 'cleans' (or 'sanitizes') the user's field before actually handling it
- Structured Query Language (SQL)
    - SQL is a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS).
- Non SQL (NoSQL)
    - A NoSQL (originally referring to "non-SQL" or "non-relational") database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases
- MongoDB
    - MongoDB is a cross-platform document-oriented database program. 
- Mongoose
    - Mongoose organizes a non-relational data structure in a manner that can be parsed. 
- record
    - A record is a collection of fields, possibly of different data types, typically in fixed number and sequence.
- document
    - A document db is a type of non-relational db that is designed to store and query data as JSON-like documents.
- Object Relation Mapping (ORM)
    - Object-relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages.
