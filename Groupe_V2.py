import mysql.connector as mysql

db = mysql.connect(host = "localhost",database = "etudiants",user = "root",password = "")
cursor = db.cursor()

class Groupe :
    def __init__(self,id):
        self._id = id

    def ajouter(self,obj):
        cursor.execute("INSERT INTO groupe VALUES(%s)",(obj._id,))
        db.commit()


    @classmethod
    def affich_gr(self):
        cursor.execute(f'SELECT * FROM groupe')
        grp = cursor.fetchall()
        return grp

