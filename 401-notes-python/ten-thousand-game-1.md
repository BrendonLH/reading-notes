# Ten Thousand Game 1 (Reading Notes 06)

## How to Use Random Module

- the random module in python supports many differnet functions, one of the most used is the ability to randomize numbers.
    - Randint(low,high)
        - takes two arguments, and returns a random integer from the lowest to the highest number. 
            > **example:**
            >
            >Import random
            >
            > print(random.randint(1,10))
            >
            > console--> 7
    - Choice(list)
        - Choice function returns a random element from a list
            > **example:**
            >
            >import random
            >
            >list = [ 'item1' , 'item2', 'item3' ]
            >
            > print(random.choice(list))
            >
            > console--> item2

## What is Risk Analysis

- risk analysis is identifying risks in applications/software and giving them priority in testing. 

- Using risk analysis allows a dev to highlight problem areas and help mitigate any risks. this allows the dev the create solutions to potential problems at the beggining rather than fixing a problem during production.

- some tools for helping with risk management: 
    1. conduct risk analysis meetings
    2. use max resources to mitigate high risks
    3. create a risk database to be used in the future
    4. set risk magnitude indicators:
        - low 
            - no financial or external exposure/loss
        - med
            - not desirable but tolerable, can lead to minor financial loss
        - high
            - critical, not tolerable, can face financial loss

- perspective of risk assessment
    1. Effect - event, condition or action and its impact
    
    2. Cause - Looking for reason of effect , cause or impact

    3. Liklihood - to identify if a requirement will be 
    satisfied. will the product do what it is supposed to do.

## Test Coverage
from the article here is my uderstanding: 

test coverage is not simply a number you should be aiming for. this can result in bad tests just to satisfy the testing coverage requirement lets say 80%. Bad tests are exactly that, bad tests. 

instead, we should be making tests that can allow us to change code without causing production issues and tests should be catching bugs before they get into production. 

overall, making our tests more meanigful is what I gathered from this article.



## Things I want to know more about

are there risk analysis forms in software development? When we need to save anything related to risk analysis, are risks stored somehwere that costs money? what exactly are risk meetings and is that part of the agile environment? 