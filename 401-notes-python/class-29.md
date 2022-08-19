# Readings (class-29)

## Topic : Django Custom User

### Django Best Practices: Custom User Model
- Django comes with its own built in user authentication. It is reccomended that devs build out their own custom models as it will have a lot more flexability. 
- (key Terms)
    - AbstractUser
        - A model that allows building a user model that is based off the AbstractBaseUser using default configuration.
    - AbstractBaseUser
        - This is the original Base for abstract models. This allows the most functionality and methods but a ton more work.
- (Additional Notes)
  - Custom forms are the reccomended way to build logins, using the default method is mainly used for tutorials and instruction or just for something really fast.

### Django X
- (summary of article)
  - the article is the github readme, so I will be summarizing and using information from other sources.
  - Django X is a starter framework. It was built with the idea in mind for begginers to be able to better use forms and patterns other than djangos built in's. 

## Things I want to Know more about
- (pertains to whole topic of reading)
  - Now that I know how to build pip packages, I am really considering building a package that can be installed for django apps that would work similar to bootstrap, where you can install the package and when you run some functions it will build out a html file with a starter template, css file and js file and link them all.
  - I know how static files work with django and just got all my static files linked, so I think I can make a package that can automate all that for django.
  - I could even make it so devs who dont like front end but need it to be mobile responsive, could just use a generated template and it is already responsive and the dev can focus on backend and just fill in the blank for the HTML file.  