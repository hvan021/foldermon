import os
from filesystem import FileSystem
from db import DB
from cmsutil import debug
#import sys
import time
import logging
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class FileMonHandler(FileSystemEventHandler):

    def on_modified():
        pass


if __name__ == "__main__":

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








    # see this for customized event handler http://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes
    # http://stackoverflow.com/questions/11883336/detect-file-creation-with-watchdog

    logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = cmsfolderpath
    event_handler = MyEventHandler(cmsfolderpath)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


class MyEventHandler(FileSystemEventHandler):
    def __init__(self, filename):
        #self.observer = observer
        self.filename = filename

    def on_created(self, event):
        print "e=", event
        #if not event.is_directory and event.src_path.endswith(self.filename):
            #print "file created"
            #self.observer.stop()


