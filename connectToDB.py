import sqlite3

class DataBase():
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cor = self.conn.cursor()
    
    def get_data(self,key):
        qurry = self.cor.execute(f"select  Rs , Name from 'Food' where Type ='{key}'").fetchall()
        return qurry

