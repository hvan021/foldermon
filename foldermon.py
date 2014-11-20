import os
from FileSystem import FileSystem
from db import DB

cmsfolderpath = "/home/huy/foldermon"
cmsfolder = FileSystem(cmsfolderpath)

print cmsfolder

print cmsfolder.get_attr()

children = cmsfolder.get_children()
print children


init_db_table_query =  '''CREATE TABLE IF NOT EXISTS filesytem
                        (id integer primary key, path text, md5checksum text default null,
                        client_id integer not null default None,
                        ctime integer, mtime integer, atime integer,
                        synctime integer not null default 0)'''

db = DB()
db.query(init_db_table_query)



def init_db():
    print "creating db file"
    conn = sqlite3.connect(dbfilename)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS dirs
                (id integer primary key, client_id integer not null default 0, dirname text, ctime integer, mtime integer, atime integer, synctime integer NOT NULL DEFAULT 0)''')

    # Insert a row of data
    # c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    print "insert items into db"
    dir_objs = [Folder(os.path.join(cmsdir, child_dir)) for child_dir in child_dirs]
    dirvals = [d.getval() for d in dir_objs]
    # dirval = for(Folder(os.path.join(cmsdir, child_dir)) child_dir in child_dirs)
    c.executemany('INSERT INTO dirs(client_id, dirname, ctime, mtime, atime) VALUES(?,?,?,?,?)', dirvals)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

