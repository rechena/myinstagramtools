#/usr/bin/env python

from instagram.client import InstagramAPI
import urllib, os, sys
import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

#Instagram Details
access_token = "<add your token here>"
client_secret = "<add your secret here>"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

#Evernote Details
auth_token = "<add your token here>"

client = EvernoteClient(token=auth_token, sandbox=False)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print "Is my Evernote API version up to date? ", str(version_ok)
print ""
if not version_ok:
    exit(1)

note_store = client.get_note_store()

photos = []
tagtosearch = "<add the tag to search here>"
newphotos = 0
currentphotos = 0
path = os.path.join('/Users/rechena/Desktop/'+tagtosearch)
if not os.path.exists(path):
    print "[INFO] %s does not exist, creating..." % path
    os.makedirs(path)

recent_media, next = api.tag_recent_media(tag_name=tagtosearch, count=1)
print "Starting process..."
while next:
    more_media, next = api.tag_recent_media(with_next_url=next, tag_name=tagtosearch)
    # print more_media
    recent_media.extend(more_media)
    for i, media in enumerate(more_media):
        try:
            phototitle = media.caption.text.split("#")
        except Exception as e:
            print e
            pass
    	location = media.images['standard_resolution'].url
    	name = "%s.jpg" % media.id

        #Debug prints...
    	# print phototitle
        # print "%s:%s:%s" % (i, media.images['standard_resolution'].url, media.id)

    	photos.append(location)
        if not os.path.exists(path+"/"+name):
            print "[INFO] New photo found...downloading..."
            print "[OK] Photo name:", name
            newphotos += 1
            urllib.urlretrieve(location, path+"/"+name)
            #Creating Evernote Note
            print "[INFO] Creating new Note in Evernote"
            note = Types.Note()
            if ((phototitle[0] == "") or (len(phototitle[0]) > 100)):
                note.title = "Instagram from %s" % tagtosearch
            else:
                note.title = phototitle[0].rstrip().encode("utf-8")
            imagetoadd = os.path.join(path, name)
            image = open(imagetoadd, 'rb').read()
            md5 = hashlib.md5()
            md5.update(image)
            hash = md5.digest()

            data = Types.Data()
            data.size = len(image)
            data.bodyHash = hash
            data.body = image

            resource = Types.Resource()
            resource.mime = 'image/jpg'
            resource.data = data
            note.resources = [resource]
            hash_hex = binascii.hexlify(hash)
            note.content = '<?xml version="1.0" encoding="UTF-8"?>'
            note.content += '<!DOCTYPE en-note SYSTEM ' \
                '"http://xml.evernote.com/pub/enml2.dtd">'
            note.content += '<en-note>Instagram:<br/>'
            note.content += '<en-media type="image/png" hash="' + hash_hex + '"/>'
            note.content += '</en-note>'
            created_note = note_store.createNote(note)
            print "Successfully created a new note with GUID: ", created_note.guid
        else:
            # print "Photo already exists"
            currentphotos += 1
        # sys.stdout.write(".")

# print len(photos)
print "Current photos:", currentphotos
print "New photos:", newphotos