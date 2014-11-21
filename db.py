import sqlite3
import sys

class DB(object):

    def __init__(self, dbfilename = 'db.db'):
        self.dbfilename = dbfilename
        #cwd = os.getcwd()
        #if not os.path.isfile(os.path.join(cwd, self.dbfilename)):
            #init_db()

    def query(self, query):
        try:
            conn = sqlite3.connect(self.dbfilename)
            c = conn.cursor()
            c.execute(query)
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


