import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Laplateforme"
)

# Création de l'objet cursor
cursor = mydb.cursor()

# Exécution de la requête 
query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()

# afficher le resultat
superficie_totale = result[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

cursor.close()
mydb.close()

