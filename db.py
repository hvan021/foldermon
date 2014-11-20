import sqlite3
import sys

class DB(object):

    def __init__(self, dbfilename = 'db.db'):
        self.dbfilename = dbfilename

    def query(self, query):
        try:
            conn = sqlite3.connect(self.dbfilename)
            c = conn.cursor()
            c.execute(query)
            #c.execute('''CREATE TABLE IF NOT EXISTS filesytem
                        #(id integer primary key, path text, md5checksum text default null,
                        #client_id integer not null default None,
                        #ctime integer, mtime integer, atime integer,
                        #synctime integer not null default 0)''')
            conn.commit()
            conn.close()
        except :
            #"ERROR! %s - \n%s", sys.exc_info()[0], query
            print "ERROR! %s - \n%s" % (sys.exc_info()[0], query)

    def multi_query(query, vals):
        conn = sqlite3.connect(self.dbfilename)
        c = conn.cursor()
        c.executemany(query, vals)
        conn.commit()
        conn.close()


