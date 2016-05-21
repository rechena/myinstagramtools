# myinstagramtools
For this you'll need: 
* Evernote API Python:
https://dev.evernote.com/doc/start/python.php
* Instagram API Python:
https://github.com/facebookarchive/python-instagram

## Intro
This is a script that I've done to replace my IFFFT tools. 
It will search for a specific TAG in Instagram, dowload the big resolution image and create a Evernote Note in the default Evernote Notebook. 

### Notes
* It will create the Folder defined in the path if not exists
* It will create the note with the Title from the Instagram till the first #tag 
.* e.g: "This is a test #tag", the note tilte will be "This is a test"
.* If theres no title it will create with "Instagram from <tag to search>"

### TODO
Lots of stuff, this a small, and start script... 
