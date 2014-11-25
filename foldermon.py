import os
from FileSystem import FileSystem
from db import DB
from cmsutil import debug

cmsfolderpath = "/home/huy/foldermon"
dbfilename = 'db.db'

cmsfolder = FileSystem(cmsfolderpath)

debug(cmsfolder)
debug(cmsfolder.get_attr())

children = cmsfolder.get_children()
debug(children)

if not os.path.isfile(os.path.join(os.getcwd(), dbfilename)):
    init_db_table_query =  '''
                            CREATE TABLE IF NOT EXISTS filesytem (
                            id INTEGER PRIMARY KEY,
                            path TEXT,
                            md5checksum TEXT,
                            client_id INTEGER
                            ctime INTEGER,
                            mtime INTEGER,
                            atime INTEGER,
                            synctime DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                            '''

    db = DB()
    db.query(init_db_table_query)


