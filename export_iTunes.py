# Kevin Camidge
# 7/5/2016

import os, shutil, xmlutil


start_dir = "C:\\Users\\Kevin\\Desktop\\playlist\\new\\";
dest_dir = "C:\\Users\\Kevin\\Desktop\\playlist\\old\\";
# xmlfilename = "Throwbacks.xml";
new_xml = xmlutil.XMLFile("NewPlaylist.xml",
                          start_dir)
if os.path.isfile(dest_dir + "OldPlaylist.xml"):
    old_xml = xmlutil.XMLFile("OldPlaylist.xml",
                              dest_dir)
else:
    xmlutil.addAll(new_xml,
                   dest_dir)
    shutil.copy("C:\\Users\\Kevin\\Desktop\\playlist\\new\\NewPlaylist.xml",
                "C:\\Users\\Kevin\\Desktop\\playlist\\old\\OldPlaylist.xml")

z = []
print(new_xml.getFilepathList())
print("\n")
print(xmlutil.getAbsFilepathList(new_xml.getFilepathList()))
