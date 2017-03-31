# Kevin Camidge
# 9/12/2016

import shutil, os
from xml.dom import minidom

class XMLFile:
    def __init__(self, fileName, dest):
        self.fileName = fileName
        self.dest = dest
        self.filePath = dest + fileName
        self.iTunesFilePathList = []
        self.destinationFilePathList = []
        self.parseFileForLocations()

    # Searches the xml for the file locations
    def parseFileForLocations(self):
        # minidom.parse("filePath to xml file")
        xmlDoc = minidom.parse(self.filePath)
        plist = xmlDoc.getElementsByTagName("plist")[0]
        dict1 = plist.getElementsByTagName("dict")[0]
        dict2 = dict1.getElementsByTagName("dict")[0]
        dict3 = dict2.getElementsByTagName("dict")
        for tag in dict3:
            key = tag.getElementsByTagName("key")
            for x in key:
                text = x.firstChild.data
                if (text == "Location"):
                    filePathFull = x.nextSibling.firstChild.data
                    filePath = filePathFull[17:]
                    filePath = getAbsFilePath(filePath)
                    self.destinationFilePathList.append(self.dest + filePath[16:])
                    self.iTunesFilePathList.append(filePath)





#### This block deals with converting the xml filePath into a usable windows filePath
def replace_chars(filePath):
    filePath = filePath.replace("%20"," ")
    filePath = filePath.replace("%C3%A9","é")
    filePath = filePath.replace("%C3%A1","á")
    return filePath
def getAbsFilePath(filePath):
    absFilePath = os.path.abspath(filePath)
    absFilePath = replace_chars(absFilePath)
    return absFilePath
def getAbsFilePathList(list):
    new_list = []
    for path in list:
        new_list.append(getAbsFilePath(path))
    return new_list
####


def addFiles(new_xml, dest_dir):
    # If the folder doesn't contain an xml file, delete all files and copy over new files including xml
    if not os.path.isfile(dest_dir + "OldPlaylist.xml"):
        #deleteAll(dest_dir)
        addAll(new_xml, dest_dir)
        shutil.copy(new_xml.filePath, dest_dir + "OldPlaylist.xml")
        print("All files have been copied to the desired location.")
        return
    else:
        old_xml = XMLFile("OldPlaylist.xml", dest_dir)
        print("Nothing happens")


# Checks if $filePath is present in $xmlDoc
def isPresent(filePath, xmlDoc):
    filePathList = xmlDoc.iTunesFilePathList
    for path in filePathList:
        if(path == filePath):
            return 1
    return 0


# Delete files present in $old_xmlDoc that are not present in $new_xmlDoc
def deleteRemovedFiles(old_xmlDoc, new_xmlDoc, location):
    present = 0
    old_list = old_xmlDoc.iTunesFilePathList
    new_list = new_xmlDoc.iTunesFilePathList
    for path in old_list:
        if(path not in new_list):
            # remove new file location, not itunes location
            os.remove(path)


# Adds files present in $new_xmldoc that are not present in $old_xmlDoc
def addNewFiles(old_xmlDoc, new_xmlDoc, dest):
    old_list = old_xmlDoc.iTunesFilePathList
    new_list = new_xmlDoc.iTunesFilePathList
    for path in new_list:
        if(path not in old_list):
            shutil.copy(getAbsFilePath(path), dest)
    return 0


# Adds all files from $xmlDoc
def addAll(xmlDoc, dest):
    filePathList = xmlDoc.iTunesFilePathList
    absFilePathList = getAbsFilePathList(filePathList)
    for filePath in absFilePathList:
        shutil.copy(filePath, dest)
