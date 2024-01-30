import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = " root",
    password = "1234",
    database = " Laplateforme"
)

cursor = mydb.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

results = cursor.fetchall()

for row in results :
    nom, capacite = row
    print(f"Nom:{nom}, Capacite:{capacite}")

cursor.close()
mydb.close()    