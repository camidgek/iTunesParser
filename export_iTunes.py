# Kevin Camidge
# 7/5/2016

import os, shutil, xmlutil


start_dir = "\\playlist\\new\\"
start_filename = "NewPlaylist.xml"
dest_dir = "\\playlist\\old\\"


new_xml = xmlutil.XMLFile(start_filename, start_dir)

xmlutil.addFiles(new_xml, dest_dir)


# if os.path.isfile(dest_dir + "OldPlaylist.xml"):
#     old_xml = xmlutil.XMLFile("OldPlaylist.xml", dest_dir)
# else:
#     xmlutil.addAll(new_xml, dest_dir)
#     shutil.copy(start_dir + "NewPlaylist.xml", dest_dir + "OldPlaylist.xml")


# print(new_xml.getFilepathList())
# print("\n")
# print(new_xml.getFilepathList())
