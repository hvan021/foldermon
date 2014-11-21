#import sys
import os
#import datetime
import hashlib
import cmsutil
# import time

# This class represents the file system of the os
# it wrap the feature and attributes of files and folders of any OS
class FileSystem(object):

    # path = "~/ClientFiles"
    #type = 'f'

    def __init__(self, path):
        self.path = path
        if os.path.isdir(path):
            self.type = 'd'
        elif os.path.isfile(path):
            self.type =  'f'
        else:
            pass

    def get_name(self):
        #root, name = os.path.split(self.path)
        name = os.path.basename(self.path)
        return name

    def get_children(self):
        if self.type == 'd':
            try:
                children = [FileSystem(os.path.join(self.path, childname)) for childname in os.listdir(self.path) if not (childname.startswith('~') or childname.startswith('.'))]
                return children
            except :
                print "cannot get children for folder %s, exception %s", self.path, sys.exc_info()

    def checksum(self):
        if self.type == 'f':
            blocksize = 65536
            md5 = hashlib.md5()
            f = open(self.path)
            buf = f.read(blocksize)
            while len(buf) > 0:
                md5.update(buf)
                buf = f.read(blocksize)
            return  md5.hexdigest()

    def get_size(self):
        if(self.type == 'f'):
            pass

    def get_cms_client_id_from_dirname(self):
        try:
            root, dirname = os.path.split(self.path)
            client_id = dirname.split("-")[0].strip()
            #if self.is_int(client_id):
                #return int(client_id)
            #print client_id
            if client_id.isdigit():
                return int(client_id)
        except:
            return None

    def getval(self):
        dirstat = os.stat(self.path)
        # print time.ctime(dirstat.st_mtime)
        # print time.localtime()
        # print time.gmtime()
        return (self.get_cms_client_id_from_dirname(), self.path, dirstat.st_ctime, dirstat.st_mtime, dirstat.st_atime)

    def get_attr(self):
        dirstat = os.stat(self.path)
        #print dirstat
        client_id = self.get_cms_client_id_from_dirname()
        ctime = cmsutil.strfunixtime(dirstat.st_ctime)
        mtime = cmsutil.strfunixtime(dirstat.st_mtime)
        atime = cmsutil.strfunixtime(dirstat.st_atime)
        md5checksum = self.checksum()
        return (client_id, self.path, self.type, ctime, mtime, atime, md5checksum)

    def get_parent(self):
        #return os.path.split(self.path)
        return os.path.dirname(self.path)

    def __str__(self):
        #dirstat = os.stat(self.path)
        #return "%s | type: %s | ctime: %s  - mtime: %s - atime: %s | md5: %s\n" % (self.path, self.type, FileSystem.strfunixtime(dirstat.st_ctime), FileSystem.strfunixtime(dirstat.st_mtime), FileSystem.strfunixtime(dirstat.st_atime), self.checksum())
        #return "%s | type: %s | ctime: %s  - mtime: %s - atime: %s\n" % (self.path, self.type, FileSystem.strfunixtime(dirstat.st_ctime), FileSystem.strfunixtime(dirstat.st_mtime), FileSystem.strfunixtime(dirstat.st_atime))
        return "client_id: %s| path: %s | type: %s | ctime: %s  - mtime: %s - atime: %s | md5: %s\n" % self.get_attr()

    def __unicode__(self):
        #dirstat = os.stat(self.path)
        #return u"%s |type: %s | ctime: %s  - mtime: %s - atime: %s" % (self.path,self,type, FileSystem.strfunixtime(dirstat.st_ctime), FileSystem.strfunixtime(dirstat.st_mtime), FileSystem.strfunixtime(dirstat.st_atime))
        return u"client_id: %s| path: %s | type: %s | ctime: %s  - mtime: %s - atime: %s | md5: %s\n" % self.get_attr()

    def __repr__(self):
        return self.__str__()




    #def print_child_dirs(self):
        #for d in self.get_child_dirs():
            #dirstat = os.stat(os.path.join(self.path, d))
            #print "%s | ctime: %s  - mtime: %s - atime: %s" % (d, Folder.strfunixtime(dirstat.st_ctime), Folder.strfunixtime(dirstat.st_mtime), Folder.strfunixtime(dirstat.st_atime))

    #def get_child_dirs(self):
        #if self.type == 'd':
            #try:
                ##print os.listdir(self.path)

                ## get dirnames with client number only, also sort them by client number
                ##dirnames = sorted([d for d in os.listdir(self.path) if Folder.is_int(d.split("-")[0]) and os.path.isdir(os.path.join(self.path, d))], key=lambda dname: int(dname.split("-")[0]))


                ## get all dirnames without any filter
                #dirnames = [d for d in os.listdir(self.path)]


                #return dirnames
            ##except WindowsError:
            #except:
                #print "Folder %s not exists" % self.path

    #def get_child_files(self):
        #try:
            #files = [File(os.path.join(self.path, f)) for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f)) and not (f.startswith('~') or f.startswith('.'))]  # create new File
            #return files
        #except:
            #print "Cannot get files in folder %s" % self.path

    #@staticmethod
    #def is_int(s):
        ## print s
        #try:
            #int(s)
            #return True
        #except ValueError:
            #return False

    #@staticmethod
    #def strfunixtime(t):
        #return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
