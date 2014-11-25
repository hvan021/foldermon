import os
from filesystem import FileSystem
from db import DB
from cmsutil import debug

cmsfolderpath = "/home/huy/foldermon"
dbfilename = 'db.db'

cmsfolder = FileSystem(cmsfolderpath)

#debug(cmsfolder)
#debug(cmsfolder.get_attr())

children = cmsfolder.get_children()
#debug(children)

if not os.path.isfile(os.path.join(os.getcwd(), dbfilename)):
    init_db_table_query =  '''
                            CREATE TABLE IF NOT EXISTS filesystem (
                            id INTEGER PRIMARY KEY,
                            client_id INTEGER,
                            path TEXT,
                            type TEXT,
                            md5checksum TEXT,
                            ctime INTEGER,
                            mtime INTEGER,
                            atime INTEGER,
                            synctime DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                            '''

    db = DB()
    db.query(init_db_table_query)


    init_fs_query = '''
                    INSERT INTO filesystem(client_id, path, type, md5checksum, ctime, mtime, atime)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    '''

    db.query(init_fs_query, cmsfolder.get_attr())
    db.multi_query(init_fs_query, [child.get_attr() for child in cmsfolder.get_children()])


db = DB()
db_out_query = '''
                SELECT * FROM filesystem
               '''
c = db.query(db_out_query)
#print c
for result in c:
    print result

