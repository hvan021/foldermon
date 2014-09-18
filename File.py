import os
import win32api
import win32con
import win32security


class File(object):

    def __init__(self, path):
        self.path = path

    def get_owner(self):
        # print "I am", win32api.GetUserNameEx(win32con.NameSamCompatible)

        sd = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)

        # print "File owned by %s\\%s" % (domain, name)
        return name

    def __str__(self):
        root, fname = os.path.split(self.path)
        return "%s - owned by: %s" % (fname, self.get_owner())


