# Kevin Camidge
# 9/12/2016

import shutil, os
from xml.dom import minidom

class XMLFile:
    def __init__(self, filename, mydir):
        self.myfilename = filename
        self.mydir = mydir
        self.myfilepath = mydir + filename
        self.mp3filepathlist = []
        self.parseFileForLocations()

    def parseFileForLocations(self):
        # minidom.parse("filepath to xml file")
        xmldoc = minidom.parse(self.myfilepath)
        plist = xmldoc.getElementsByTagName("plist")[0]
        dict1 = plist.getElementsByTagName("dict")[0]
        dict2 = dict1.getElementsByTagName("dict")[0]
        dict3 = dict2.getElementsByTagName("dict")
        for tag in dict3:
            key = tag.getElementsByTagName("key")
            for x in key:
                text = x.firstChild.data
                if (text == "Location"):
                    filepathfull = x.nextSibling.firstChild.data
                    filepath = filepathfull[17:]
                    filepath = getAbsFilepath(filepath)
                    self.mp3filepathlist.append(filepath)

    def getFilepathList(self):
        return self.mp3filepathlist


#### This block deals with converting the xml filepath into a usable windows filepath
def replace_chars(filepath):
    filepath = filepath.replace("%20"," ")
    filepath = filepath.replace("%C3%A9","é")
    filepath = filepath.replace("%C3%A1","á")
    return filepath
def getAbsFilepath(filepath):
    absfilepath = os.path.abspath(filepath)
    absfilepath = replace_chars(absfilepath)
    return absfilepath
def getAbsFilepathList(list):
    newlist = []
    for path in list:
        newlist.append(getAbsFilepath(path))
    return newlist
####


def addFiles(new_xml, dest_dir):
    # If the folder doesn't contain an xml file, delete all files and copy over new files including xml
    if not os.path.isfile(dest_dir + "OldPlaylist.xml"):
        #deleteAll(dest_dir)
        addAll(new_xml, dest_dir)
        shutil.copy(new_xml.filepath, dest_dir + "OldPlaylist.xml")
        print("All files have been copied to the desired location.")
        return
    else:
        old_xml = XMLFile("OldPlaylist.xml", dest_dir)
        print("Nothing happens")



# Checks if $filepath is present in $xmldoc
def isPresent(filepath, xmldoc):
    filepathlist = xmldoc.mp3filepathlist
    for path in filepathlist:
        if(path == filepath):
            return 1
    return 0


# Delete files present in $old_xmldoc that are not present in $new_xmldoc			
def deleteRemovedFiles(old_xmldoc, new_xmldoc, location):
    present = 0
    old_list = old_xmldoc.mp3filepathlist
    new_list = new_xmldoc.mp3filepathlist
    for path in old_list:
        if(path not in new_list):
            # remove new file location, not itunes location
            os.remove(path)


# Adds files present in $new_xmldoc that are not present in $old_xmldoc
def addNewFiles(old_xmldoc, new_xmldoc, dest):
    old_list = old_xmldoc.mp3filepathlist
    new_list = new_xmldoc.mp3filepathlist
    for path in new_list:
        if(path not in old_list):
            shutil.copy(getAbsFilepath(path), dest)
    return 0


# Adds all files from $xmldoc
def addAll(xmldoc, dest):
    filepathlist = xmldoc.getFilepathList()
    absfilepathlist = getAbsFilepathList(filepathlist)
    for filepath in absfilepathlist:
        shutil.copy(filepath, dest)
