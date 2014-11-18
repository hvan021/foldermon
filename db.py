import sqlite3

class DB(object):

    dbfilename = 'db.db'
    def __init__(self, dbfilename):
        self.dbfilename = dbfilename

    def query(query):
        conn = sqlite3.connect(self.dbfilename)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()
