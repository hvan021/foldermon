import os
import datetime


class Folder(object):

    path = "~/ClientFiles"

    def __init__(self):
        pass

    def get_child_dir(self):
        dirnames = sorted([d for d in os.listdir(self.path) if self.is_int(d.split("-")[0]) and os.path.isdir(os.path.join(self.path, d))], key=lambda dname: int(dname.split("-")[0]))
        for d in dirnames:
            dirstat = os.stat(os.path.join(self.path, d))
            print "%s | ctime: %s  - mtime: %s - atime: %s" % (d, self.strfunixtime(dirstat.st_ctime), self.strfunixtime(dirstat.st_mtime), self.strfunixtime(dirstat.st_atime))

    # @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def strfunixtime(t):
        return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
