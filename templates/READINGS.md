# Readings React Readings 4

## Topic : React/Next JS deployment

### Dynamic Routes
- (summary of article)
    - Dynamic routes allow us to use multiple routes as objects instead of explicitly using a route path. With dynamic routes we can pre-render pages using external data.


### Deployement
- Next.js was developed by the same creators as Vercel. This makes deploying next.js applications easy and fluid.
- (key Terms)
    - Vercel
        - Serverless platform for static and hybrid web applications. 
    Deploying: 
        1. Create Vercel account
        2. install vercel for github and allow access to all repos
        3. import the next js application
        4. use the defualt values (vercel auto detects)
        5. stand by while vercel builds the application
- I have used vercel alot, I really like it, it is very simple and quick. I will be building my new portfolio and deploying with vercel.

## Things I want to Know more about
- (pertains to whole topic of reading)
    - I happened to stumble on domain name stuff with AWS. When it comes to deploying applications, should I be registering domain names for both the server and the front end facing site? Or do I just need to register the front end domain name? Can the server and db just stricly server data and not need a registered domain. I ask because we built our API backend and I noticed on other API sites, they are all registered. Would it be better to just do a django front and backend, deploy to AWS and then register one domain name? or do I not need to register the Server/API? 

    - I also am looking at HTTP VS HTTPS and noticed more security features, so should I register the domain so I can get a Certificate to route everything that comes through as HTTP to an HTTPS request for security? I know we are only doing HTTP stuff, its just interesting as security is a big deal nowadays. 