# Readings (class-34)

## Topic : API Deployement

### Django Settings Best Practices
- There are many different ways to configure settings for django applications.
- (key Terms)
    - Settings.py file
        - Holds settings configurations such as allowed hosts, what database is being used ect.
    - Environment Variables
        - This is how you keep sensitive information from being public. Instead of storing username and password for DB's, you can store them in a .env file and import them into the settings file as a variable.
- Environment variables are a great place to keep sensitive information. Hosts like heroku use environment variables to keep database access, hosts and port numbers secret for security.

### SSH Tutorial
- SSH is a replacement for unencrypted Telnet and ensures all communication to and from remote servers in an encrypted manner.
- (key Terms)
    - Symmetric Encryption
        - Encryption where a secret key is used for both encryption and decryption
    - Asymmetric Encryption
        - Uses two seperate keys for both encryption and decryption 
    - Hashing
        - used in SSH because they are not made to be decrypted, this makes them near impossible to reverse.
- (additional notes)

## Things I want to Know more about
- to be honest, SSH seems kinda boring to me. Is it something I can use to send private information between servers? is that the purpose? How is something like this used to prevent security for notorious means. Can I open up two SSH between two computers over ports? I get the security and why we might need it, but is this also used for nefarious means? 