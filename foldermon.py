import os
from FileSystem import FileSystem

cmsfolderpath = "/home/huy/foldermon"
cmsfolder = FileSystem(cmsfolderpath)

print cmsfolder

print cmsfolder.type

children = cmsfolder.get_children()
print children
