# Class 401-Javascript Reading Notes

## Hooks API

## Table of COntents

* [Questions](###questions)
* [Vocabulary Terms](###vocabulary-terms)

### Questions

1. Why do we not need more .html pages in a multi-page React app?
    - we can use react Routes to change the url path which will render different components. 

2. If we wanted a component to show up on every page, where would we put it and why?
    Outside the <BrowserRouter/>
    Inside the <BrowserRouter />, outside a <Route />
    Inside a <Route />

    - we woud want to wrap the route, so that all the props are passed down to everything inside BrowserRouter.  

3. What does props.children contain?
<parent>  
    <child> 
       <items> ---------> this.props.children, anything in this is this.props.children, (lists, componenets, functions, ect.) 
    </child>
</parent>

    

### Vocabulary Terms

**Composition:** 
    - Allows You to make more functionality by combining functions such as map and filter together.

**Children / Child Components:**
    - Components that use functions and props from a parent to manipulate and chnage the parent state.

**Hash Routing:** 
    - uses URL hash, it puts no limitations on supported browsers or web server. Server-side routing is independent from client-side routing.
    
**Link Routing:** 
    - used to navigate the different parts of an application by way of hyperlinks. 


Which 3 things had you heard about previously and now have better clarity on?
 - hashrouting, linkrouting and browserRouter
Which 3 things are you hoping to learn more about in the upcoming lecture/demo?
 - how to pass data around better
 - better styling methods
 - animations with react
What are you most excited about trying to implement or see how it works?
 - anything about passing data around

