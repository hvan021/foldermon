import sqlite3
import sys

class DB(object):

    def __init__(self, dbfilename = 'db.db'):
        self.dbfilename = dbfilename
        #cwd = os.getcwd()
        #if not os.path.isfile(os.path.join(cwd, self.dbfilename)):
            #init_db()

    def query(self, query, params = None):
        try:
            conn = sqlite3.connect(self.dbfilename)
            c = conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            conn.commit()
            vals = c.fetchall()
            conn.close()
            return vals
        except :
            #"ERROR! %s - \n%s", sys.exc_info()[0], query
            print "ERROR! %s - \n%s" % (sys.exc_info()[0], query)

    def multi_query(self, query, params):
        try:
            conn = sqlite3.connect(self.dbfilename)
            c = conn.cursor()
            c.executemany(query, params)
            conn.commit()
            vals = c.fetchall()
            conn.close()
            return vals
        except:
            print "ERROR! %s - \n%s" % (sys.exc_info()[0], query)



