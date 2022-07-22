# Readings (class-19)

## Topic : Automation

### Python Regular Expressions Tutorial
- (summary of article)
  - Regular Expressions allow for text pattern matching. the 're' imported module has many powerful built in methods to help with finding text
- (key Terms)
    - re
        - Imported module
        - allows access to methods
          - re.search
            - looks through a string for matching text pattern
          - group
            - allows a regular expression to get parts of the matching string.
          - re.findall
            - finds all matching and returns it as a list of strings.
- (additional notes)
  - After reading this article, now I see how I can implement txt files or even web scraping better using re module. I can just save everything into a list or a big string and then use re to sift through everything for what I need, change/extract it.

### Shutil
- (summary of article)
  - shutil has higher level operations such as copying and archiving files.
- (key Terms)
    - copyfile
        - copies a file and creates a new copied file
        - raises an error if you dont have permission
  
- (additional notes)
  - From my understanding, I think shutil makes it so you get the high level information of a file/directory. 're' gets the actual information of the file, whereas 'shutil' handles the actual files/directory of the information. 


## Things I want to Know more about
- (pertains to whole topic of reading)
  - I think i understand the 're' ok, but the copying files (shutil), directories, what would be a good use case? like using it to show a changed file against an original? in example:  I am updating my resume, I copy the resume using shutil, use regex to modify the copied file, then display the original resume and the updated resume to see if I like the changes before I save the changes?