# reading-notes
Class 301 reading notes

# Table of Contents

[Class 1 day 1](##class-1-day-1)
[class 1 day 2](##class-001-day-2)
[Jquery Notes](##Jquery-notes-3/25/2020)
[Flexbox and Templating](##flexbox-notes)
[Interview Notes](###Interview-Questions)
[Regex Notes](###Regex-Notes)
[Lecture Notes](###Lecture-Notes)
[Partner Power Hour](###Partner-Power-Hour)
[Heroku Deployement](###Heroku-Deployement)
[Node](###Node-JS)
[Api's Continued](###Api's-Continued)


## class 001 day 1

1. Responsive web design
    a. design a web application to be mobile responsive first then work toward desktop.
    b. sections should not strain the eye when the user is reading so they can get the information they need and move on. 
    c. use @media to set the different browser lengths. 
    d. Using percentages will allow the browser to adapt to the different screen sizes rather than px being a fixed sizing or positioning on the page. 

2. let and const
    a. let will not hoist out of position like var does. it will stay local if inside a function.
    b. const will make a variable name the same and cannot be changed. 
3. SMACSS 
    a. when building CSS files create layouts.css, main.css, modules.css, reset.css, style.css, theme.css
    b. split your css into the different pages and then import into style.css so its only grabbing from one page on index.html

## class 001 day 2
    1. cp -rp starter-code lab       creates a folder with the starter code

## Jquery Notes 3/25/2020

    1. Jquery allows you to select elements, perform tasks and handle events.
        a. Jquery can grab CSS elements and also apply functions using javascript to those elements.
    2. Some common syntax: 
        a. $('li.cold') ---- the first selector is the element and the second selects the class. so every html li with a class of 'cold' will be selected.
        b. $('li.cold').addClass('incomplete'); -----this will grab every li with a class of cold and add another class to it called 'incomplete'.
        c. the nice thing about Jquery is that is cross browser supportive even for older browsers, so no need for fallback code. 
        d. You can use things like fadeIn(), fadeOut(), run click functions and many others instead of writing multiple lines of code for the same result. 
        e. when using jquery, youi typically use CSS style selecotrs
        f.when using a selector that returns multiple elements, Jquery loops through them for you so you wont need to write a loop function. 
    3. 306 - 331
        a. Jquery has a way to make sure the page and all assets have loadedbefore it runs the script. this is the ready() function. when the page is ready, the code inside will run.
        b. there is a function on() that replaced load() and makes sure all assets have been loaded before the code is ran.
        c. .html() and .text() both retrieve the content of the elements. the html will grab everything inside to include the syntax and the text will only grab the text content. using the .text() with li's will also return the spaces as well and make it look kinda wonky. 
        d. four methods to update content with Jquery: .html(), .text(), .replaceWith(), .remove(). 
    4. Ways to include Jquery
        a.when adding Jquery, make sure to have a fallback in case the CDN does not work. Have one stored with the rest of your website. 
        b. The script should be placed right before the closing body tag so that way all content is loaded before the Jquery is run. 
        
## Flexbox Notes

1. Justify-Content : aligns flex items along main axis
    1. flex-start; (default)
    2. flex-end;
    3. space-between;
    4. space-around;
2. align-items : aligns flex items along cross axis
    1. flex-start;
    2. flex-end;
    3. center;
    4. baseline;
    5. stretch; (default)
3. flex-direction : defines the direction of main axis
    1. row; (default)
    2. row-reverse;
    3. column; 
    4. column-reverse;
4. order : specifies order of items
    1. integers of ect -2,-1,0,1,2 ect ;
5. align-self : aligns flex item along cross axis overiding align-items
    1. flex-start;
    2. flex-end;
    3. center; 
    4. baseline
    5. stretch
6. flex-wrap : determines whether it wil be single line or wrapped on multiple lines
    a. nowrap; (default)
    b. wrap; 
    c. wrap-reverse;
7. flex-flow : short for flex-direction and flex-wrap
    a. use both flex-direction and flex wrap properties
8. align-content : aligns flex containers lines within flex container when there is extra space on cross axis
    a. flex-start;
    b. flex-end;
    c. center;
    d. space-between;
    e. space-around;
    f. stretch

### Interview Questions

    Practice the ability to think on your feet.
    Panel Interview, ability to think about on the fly questions per multiple departments. 
    Come across clear, Honest and Prepared.  

### Regex Notes

1. What is Regex?
    1. Regex stands for Regular Expressions
    2. Regex can be used to extract text from information
    3. Regex can be used in almost all languages
2. Anchors
    1. **^start** matches strings that start with the word **start**.
    2. **end$** matches the string that ends with **end**.
    3. you can use **^start end$** to match and exact string
    4. you can just use some string in place to look for that string as well
3. Character Classes
    1. **\d** matches a single character that is a digit
    2. **\w** matches a word character 
    3. **\s** matches a whitespace character

### Partner Power Hour
    1. Speaker
        a. JB Tellez : Instructor at codefellows :paython :Javascript
    2. Topic
        b. Telecommunicating : Dispatches From a Basement
    3. Notes 
        a. Pros and Cons of Telecommunicating
            1.Pros
                a. High Productivity
                b. Work from anywhere (with internet connection)
                c. Flow (get into the zone, able to focus, time flies by)
            2. Cons
                a. technical difficulties
                b. Housemates
                c. isolation
        b. Stratagies
            1. Balance(maintain work life balance)
                a. on the person to set a balanced schedule
                b. use the power of no (use time to recharge)
                c. Exercise
                d. Friends (prioritize)
                e. Controlling Anxiety
        c. Interpersonal Gotchas
            1. Eye Contact
                a. keep eyes on camera so appears to be interested
            2. Tired (take breaks, watch your sleep)
            3. Nice Spectrum
                a. be nice rather than not nice. 
            4. Intro/Extro/Ambo
                a. Introvert --- alone recharges batteries
                b. extrovert --- opposite of introvert

### Heroku Deployement

1. Heroku
    1.  Heroku is a cloud platform that lets develoers build and deploy apps
    2.  Use heroku login to login to the heroku CLI
    3.  npm install will create the node_modules and place the neccessary files into it
    4. acronym for dirt -data intensive realtime apoplications
2. nodeJS
    1. nodeJS allows you to build serverside and networking apps
    2. written in javascript
    3. example for porting
        a. var http = require("http");

        http.createServer(function(request, response) {
            response.writeHead(200, {"Content-Type": "text/plain"});
            response.write("It's alive!");
            response.end();
        }).listen(3000);

            this will write 'its alive' and listen for port 3000. you can even use the HTTP syntax and look up this on your smartphone as long as the server is running. 

### Node JS

    1. What is Node?
        a. Node.js is event based runtime that uses googles V8 engine and libuv library.
        b. node is not run in the browser but uses utility methods
        c. node lets us run javascript on the server.
    2. How to install node.js
        a. use a node package manager (npm) as this is the easiest way.
        b. use npm install to install the necessary packages.
    3. Install a package locally 
        a. npm init -y  will install and auto populate package.json file.
        b. npm install lodash --save will install a dependancy in the package.json

### Api's Continued
## What Google Learned From Its Quest to Build the Perfect Team
    1. What Google Learned from its Quest to Build the Perfect Team.

    The article is about team optimization in the workplace. Google created a project called Project Aristotle in order to find out why some teams were successful while others were not.

    they found that there are typically 2 kinds if team collaboration, one where there is a clear leader and the team sticks to the agenda and closes the meeting with little input from other members of the team. while the other has no clear leader, the topics of discussion can branch off of the main, people have equal opportunity to talk and collaborate, even going as far as to talk about things outside of work. 

    what Aristotle found was that the best teams all had an equal voice at the table. No one person was necessarily leading and all members were safe to address any problems. the best teams do not seperate work and life so much and were very attuned to social sensitively. 

    the main point I took away, was that the best teams are open and can talk to each other. communication is how to be successful. 