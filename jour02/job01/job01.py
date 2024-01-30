import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "Laplateforme",
)
 

cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiant")
resuts = cursor.fetchall()

for row in resuts:
    print(row)

cursor.close()
mydb.close()
