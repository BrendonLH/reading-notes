# The Command Line

## common commands

pwd - print working directory - shows me the full path of where i am at.
ls - list - lets me know what folder i am in and what is in the folder.
.. - pulls me back out of the current folder
cd - change directory - I can cd into another folder from current folder, combine cd and .. to pull me out of current folder to parent folder. 

## creating files

to make a file hidden when creating it, we use a dot(.) before the name. 

## manual pages

to get to the manual of your distribution, you invoke the command _man_.
for windows, you will need to run the terminal as admin and then install the hep documents. 

man -k uses the keyword search feature.

## file manipulation

### linux
mkdir - make a folder
touch - make a file
rmdir - removes a folder - folder must be empty first

### windows powershell
New-Item -Path 'folder name' -ItemType Directory - creates a folder with name folder name

New-Item 'new file' - creates a new file named new file. 

I work with windows powershell and linux quite regularly. There are many ways to manipulate things like your nano file, set permissions, change users, ect. these articles really covered the basics well. the cheat sheet will come in handy as sometimes switching between the two I can forget. for instance making a directory is completely different between windows and linux. There is a way to set the commands for powershell to mimic linux commands though.  