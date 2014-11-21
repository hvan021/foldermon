import os
from FileSystem import FileSystem
from db import DB
from cmsutil import debug

cmsfolderpath = "/home/huy/foldermon"
cmsfolder = FileSystem(cmsfolderpath)

debug(cmsfolder)

debug(cmsfolder.get_attr())

children = cmsfolder.get_children()
debug(children)


init_db_table_query =  '''CREATE TABLE IF NOT EXISTS filesytem
                        (id integer primary key, path text, md5checksum text default null,
                        client_id integer not null default None,
                        ctime integer, mtime integer, atime integer,
                        synctime integer not null default 0)'''

#db = DB()
#db.query(init_db_table_query)
