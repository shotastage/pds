import sqlite3
import os




class OnDb():

    database = 'random.db'

    db_instance = None

    db = None

    def __init__(self, db):
        self.database = db
        self.db_instance = sqlite3.connect(self.database)
        self.db = db_instance.cursor()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def initialize(self):
        self.db.execute('CREATE TABLE pds_meta_base(id INTEGER PRIMARY KEY AUTOINCREMENT, col STRING)')
