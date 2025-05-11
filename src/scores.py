"only for accessing the db"
import sqlite3
import os


class Scores:
    "class for db operations"
    def __init__(self,testing = False):
        dirname = os.path.dirname(__file__)

        if testing == True:
            if not os.path.exists("tests.db"):
                self.connection = sqlite3.connect(os.path.join(dirname, "tests.db"))
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    '''CREATE TABLE if not EXISTS Scores (id INTEGER PRIMARY KEY, name TEXT, score INT);''')
                self.connection.commit()
            else:
                self.connection = sqlite3.connect("tests.db")
                self.cursor = self.connection.cursor()
        else:
            if not os.path.exists("scores.db"):
                self.connection = sqlite3.connect(os.path.join(dirname, "scores.db"))
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    '''CREATE TABLE if not EXISTS Scores (id INTEGER PRIMARY KEY, name TEXT, score INT);''')
                self.connection.commit()
            else:
                self.connection = sqlite3.connect(os.path.join(dirname, "scores.db"))
                self.cursor = self.connection.cursor()

    def addscore(self, name, score):
        self.cursor.execute(
            '''INSERT into Scores (name, score) VALUES (?,?)''', (name, score))
        self.connection.commit()

    def readscore(self):
        self.cursor.execute(
            '''SELECT name,score FROM Scores ORDER BY score DESC LIMIT 5''')
        return self.cursor.fetchall()

    def resetscores(self):
        "deletes and creates a new db"
        self.cursor.execute('''DROP TABLE IF EXISTS Scores''')
        self.cursor.execute(
                '''CREATE TABLE Scores (id INTEGER PRIMARY KEY, name TEXT, score INT);''')
        self.connection.commit()