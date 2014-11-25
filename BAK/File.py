import os
if os.name == 'nt':
    import win32api
    import win32con
    import win32security


class File(object):

    def __init__(self, path):
        self.path = path

    def get_owner(self):
        # print "I am", win32api.GetUserNameEx(win32con.NameSamCompatible)

        try:
            if(os.name --'nt'):
                security_descriptor = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
                owner_sid = security_descriptor.GetSecurityDescriptorOwner()
                name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            else:
                mystat = os.stat(self.path)
                print mystat
                return 'unknown'

            # print "File owned by %s\\%s" % (domain, name)
            return name
        except:
            return 'unknown'

    def __str__(self):
        root, fname = os.path.split(self.path)
        return "%s - owned by: %s" % (fname, self.get_owner())


