import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "Laplateforme"
)

cursor = mydb.cursor()

query = "SELECT SUM(capacite) AS capacite_tototale FROM salle"
cursor.execute(query)

result = cursor.fetchone()

capacite_totale = result[0]
print(f"La capacite totale des selles est de {capacite_totale} personnes")

cursor.close()
mydb.close()