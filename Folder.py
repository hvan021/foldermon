import os
import datetime


class Folder(object):

    # path = "~/ClientFiles"

    def __init__(self, path):
        # self.path = "C:/Users/Hugh/ClientFiles"
        self.path = path

    def get_child_dirs(self):
        try:
            # print os.listdir(self.path)
            dirnames = sorted([d for d in os.listdir(self.path) if Folder.is_int(d.split("-")[0]) and os.path.isdir(os.path.join(self.path, d))], key=lambda dname: int(dname.split("-")[0]))
            return dirnames
        except WindowsError:
            print "Folder %s not exists" % self.path

    def print_child_dirs(self):
        for d in self.get_child_dirs():
            dirstat = os.stat(os.path.join(self.path, d))
            print "%s | ctime: %s  - mtime: %s - atime: %s" % (d, Folder.strfunixtime(dirstat.st_ctime), Folder.strfunixtime(dirstat.st_mtime), Folder.strfunixtime(dirstat.st_atime))

    def get_cms_client_id_from_dirname(self):
        # print os.path.dirname(self.path)
        # print os.path.relpath(self.path)
        # print os.path.split(self.path)
        # if Folder.is_int(os.path.dirname(self.path).split("-")[0]):
            # return self.path.split("-")[0]
        root, dirname = os.path.split(self.path)
        client_id = dirname.split("-")[0]
        if Folder.is_int(client_id):
            return client_id.strip()
        return 0

    def getval(self):
        dirstat = os.stat(self.path)
        return (self.get_cms_client_id_from_dirname(), self.path, dirstat.st_ctime, dirstat.st_mtime, dirstat.st_atime)

    def __str__(self):
        dirstat = os.stat(self.path)
        return "%s | ctime: %s  - mtime: %s - atime: %s\n" % (self.path, Folder.strfunixtime(dirstat.st_ctime), Folder.strfunixtime(dirstat.st_mtime), Folder.strfunixtime(dirstat.st_atime))

    def __unicode__(self):
        dirstat = os.stat(self.path)
        return u"%s | ctime: %s  - mtime: %s - atime: %s" % (self.path, Folder.strfunixtime(dirstat.st_ctime), Folder.strfunixtime(dirstat.st_mtime), Folder.strfunixtime(dirstat.st_atime))

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_int(s):
        # print s
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def strfunixtime(t):
        return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
