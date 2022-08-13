# Readings class-27

## Topic : Django Models

### Using Models
- Models are how to determine how our data will be stored and what it will look like in our database. Models have many attributes.
- (key Terms)
    - Model
        - The structure of our data.
        - field types: Size, dfaults, values, list options
    - Fields
        - Represents columns of data that are to be stored
    - Methods
        - Models can have methods
        - Using methods like str can return a string for user readability
- There are many built in things for models, One to look into is the ordering of the data using the metadata feature.

### Django Admin
- The django admin application is used to make it super easy to manage models and records. This will save lots of dev time.
- In order to use the Admin, we need to set a super user, You create a superuser by running the __python3 manage.py createsuperuser__.

- Once the superuser is created, to login, you go to the url and append admin and enter in username and password.

## Things I want to Know more about
- I really like the admin side of django. Having a built in administration is very useful it seems like. I wonder if I can create new users that I can set access to certain parts of a size similar to web tokens.