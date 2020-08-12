# Class 401-Javascript Reading Notes

## Engineering Topics

## Table of Contents

* [Engineering Topics](engineering-topics)
* [Node Ecosystem](node-ecosystem)


### Engineering Topics
1. Solving Problems

        When Solving a problems in a coding interview, you want to go into the problem with the mindset of "measure twice, cut once". It is very important to Allocate 3/4 of you're time on it just simply understanding the problem itself. 
            
        Break down the problem into babysteps. Make sure that you are translating it simply at first, then add the psuedo code, then fill in the psuedo code and finally optimize. 

2.  Act like you make 1000$/hr

        Business. The most successful people are not busy, they are focused. The difference is being busy is just wasting time for a small shot of satisfaction, being focused accomplishes things in a shorter amount of time with quality results. Being focused allows a person to work on things that are in keeping with their mission/goal. Do not waste your time being busy, use your time as if it is worth something. 
            
        Say no to more things as alot of the things you say yes to are not in line with what you really want. For every 10 ideas, say no to 9. Dont look for the good, seek out the great, saying no to things allows you to seek out more oppertunities that would have been missed if you said yes and wasted your time.  
3. How to think like a programmer

        When it comes to problems solving, Less is more. Start off by identifying the problem. If you cant describe the problem then you dont understand it. Break down the problem into smaller pieces. If something is too hard, make it simpler and then solve that and expand outward. Find a simliar problem that is easier, solve it and apply it to the harder problem. DEBUG DEBUG DEBUG. Look at where the problem is causing issues and work from there. Dont try to paint the whole picture, solve it piece by piece. Last, if you cant solve it, Google has an answer, you just gotta click search.
4. The 5 whys

        When encountering a problem, ask "why". Asking why will give a reason that can be followed up with anoyher why if needed. Asking why will eventually bring out the root problem. Make sure the answers are not vague but as specific as possible. This will allow a more apporachable solution. The goal is to create a preventative solution rather than just a bandaid for the problem at hand. 
### Node Ecosystem
    1.Why would you want to run JavaScript code outside of a browser?
        a. You can run Javascript on a server, You can build Desktop Widgets as well. Javascript run outside the browser allows us to work on server side code and un it inside the terminal as well. 
        source. https://www.quora.com/Can-you-run-JavaScript-outside-of-a-browser 

    2.What is the difference between a module and a package?
        a. A module is is a single Javascript File that has some functinality and a Package is a directory with a one or more modules inside of it and has a package.json file with info about the package.
        source.https://stackoverflow.com/questions/20008442/difference-between-a-module-and-a-package-in-node-js#:~:text=A%20module%20is%20a%20single%20JavaScript%20file%20that,package.json%20file%20which%20has%20metadata%20about%20the%20package.

    3.What does the node package manager do?
        a. Allows Javascript developers to share packages. It consists of A command line interface(CLI) and an online repository that hosts the packages.
        
    4.Provide code snippets showing 3 different ways to export a function from a node module
        1. module.exports = function (msg) { 
            console.log(msg);
        }; 
        var msg = require('./Log.js');
        msg('Hello World');

        2.  module.exports = function (firstName, lastName) {
                this.firstName = firstName;
                this.lastName = lastName;
                this.fullName = function () { 
                    return this.firstName + ' ' + this.lastName;
                }
            }
            var person = require('./Person.js');

            var person1 = new person('James', 'Bond');

            console.log(person1.fullName());
        Source. Node.JS tutorialsteacher.com