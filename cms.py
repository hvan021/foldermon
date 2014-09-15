import os
import datetime
import sqlite3

# print "cwd is %s" % os.getcwd()
# print "listdir is %s" % os.listdir(os.getcwd())

dbfilename = 'cms.db'
# cmsdir = os.getcwd()
# cmsdir = "D:/Client Files"
cmsdir = "~/ClientFiles"


def create_db():
    conn = sqlite3.connect(dbfilename)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS dirs
                (id integer primary key, client_id integer not null default 0, dirname text, ctime integer, mtime integer, atime integer, synctime integer)''')

    # Insert a row of data
    # c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def init_dirs():
    query = 'INSERT INTO dirs VALUES('
    for i in range(0, 3):
        query += '?,'
    query += '?)'
    print query
    # for fileanddirnames in os.listdir(cmsdir):
        # if os.path.isdir(fileanddirnames):
            # print fileanddirnames


def db_exec(query, values):
    conn = sqlite3.connect(dbfilename)
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    conn.close()


def add_dir_to_db(dirinfo):

if not os.path.isfile(dbfilename):
    create_db()


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def strfunixtime(t):
    return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")


# dirnames = []
# for fileanddirnames in os.listdir(cmsdir):
    # if os.path.isdir(fileanddirnames):
        # dirnames.append(fileanddirnames)

# def order_by_cid():

# print os.listdir(cmsdir)
'''
1. get all dirnames in the specified folder then
2. check if the first part before "-" is a number (client id) or not then
3. sort by client_id
'''
'''
dirnames = sorted([d for d in os.listdir(cmsdir) if is_int(d.split("-")[0]) and os.path.isdir(os.path.join(cmsdir, d))], key=lambda dname: int(dname.split("-")[0]))

for d in dirnames:
    dirstat = os.stat(os.path.join(cmsdir, d))
    print "%s | ctime: %s  - mtime: %s - atime: %s" % (d, strfunixtime(dirstat.st_ctime), strfunixtime(dirstat.st_mtime), strfunixtime(dirstat.st_atime))
'''
    # print os.stat(os.path.join(cmsdir, d))
# print dirnames

# init_dirs()

# for dirname, dirnames, filenames in os.walk('.vim'):
    # print dirname
    # print dirnames
    # print filenames
    # print path to all subdirectories first.
    # for subdirname in dirnames:
        # print os.path.join(dirname, subdirname)

    # # print path to all filenames.
    # for filename in filenames:
        # print os.path.join(dirname, filename)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    # if '.git' in dirnames:
        # # don't go into any .git directories.
        # dirnames.remove('.git')
