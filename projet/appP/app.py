from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def index():
    return "Bienvenue sur le site de création de réunions !"

# Page de création de réunion (exemple)
@app.route("/creer_reunion", methods=["GET", "POST"])
def creer_reunion():
    if request.method == "POST":
        # Traitement du formulaire de création de réunion
        # Récupérer les données du formulaire avec request.form
        # Effectuer les opérations nécessaires dans la base de données
        return "Réunion créée avec succès !"
    else:
        # Afficher le formulaire de création de réunion
        return render_template("creer_reunion.html")

if __name__ == "__main__":
    app.run()


# Connexion à MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="foo"
)

# Création de la table "meetings"
def database_projetv1():
    cursor = connection.cursor()

     cursor.execute("USE projetv1")

'''# Exécute la requête SQL pour créer la table "meetings"
cursor.execute("""
CREATE TABLE meetings (
id INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(255) NOT NULL,
description VARCHAR(255)
    )
""")'''

    # Ferme le curseur
cursor.close()

database_projetv1()

# Fermeture de la connexion à MySQL
connection.close()
