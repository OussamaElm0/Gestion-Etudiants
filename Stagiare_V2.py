import mysql.connector as mysql

db = mysql.connect(host = "localhost",database = "etudiants",user = "root",password = "")
cursor = db.cursor()

class Stagiaire :
    def __init__(self,id,name,email,groupe):
        self._id  =id
        self._name = name
        self._email = email
        self._groupe = groupe

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getGroupe(self):
        return self._groupe

    def setId(self,nId):
        self._id = nId

    def setName(self,nName):
        self._name = nName

    def setEmail(self,nEmail):
        self._email = nEmail

    def setGroupe(self,nGroupe):
        self._groupe = nGroupe

    def ajouter(self,obj):
        cursor.execute("INSERT INTO stagiaire(id,nom,email,groupe) VALUES(%s,%s,%s,%s)",
                       (obj._id,obj._name,obj._email,obj._groupe))
        db.commit()

    def supprimer(self,id):
        cursor.execute(f'DELETE FROM stagiaire WHERE id = %s',(id,))
        db.commit()

    def rechercher(self,id):
        cursor.execute(f'SELECT * FROM stagiaire WHERE id = %s',(id,))
        etu = cursor.fetchall()
        for i in etu :
            return (i[0], i[1], i[2], i[3])

    def modifier(self,id,name,email,groupe):
        cursor.execute(f'UPDATE stagiaire SET nom = %s, email = %s , groupe = %s  WHERE id = %s',
                       (self._name,self._email,self._groupe,id))
        db.commit()

    def afficher(self):
        cursor.execute(f'SELECT * FROM stagiaire')
        etu = cursor.fetchall()
        return etu

    def afficher_grp(self,groupe):
        cursor.execute(f'SELECT * FROM stagiaire where groupe = %s',(groupe,))
        grp = cursor.fetchall()
        return grp