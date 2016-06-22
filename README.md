[![Build Status](https://travis-ci.org/rechena/myinstagramtools.svg?branch=master)](https://travis-ci.org/rechena/myinstagramtools)

# myinstagramtools

## Intro
This is a script that I've done to replace my IFFFT tools. 
It will search for a specific TAG on **your account** on Instagram, download the image and create a Evernote Note in the **picked** Evernote Notebook.

*Info*: Due to the new Instagram API rules you can no longer download public tags, so this script will only search for the tag in your account!!

### Notes
* For this you'll need: 
	* Evernote API Python:
https://dev.evernote.com/doc/start/python.php
	* Instagram API Python:
https://github.com/facebookarchive/python-instagram
* It will create the Folder defined in the path if does not exists
* It will create the note with the Title from the Instagram till the first # 
* If no title it will create with "Instagram from <tag to search>"

### TODO
* ~~Pick the notebook~~ - DONE
* Cleanup...
* Lots of stuff, this a small, and start script... 
