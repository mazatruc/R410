from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__)
app.secret_key = "votre_clé_secrète"

# Page d'accueil
@app.route("/")
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



# Connexion à la base de données
conn = pymysql.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base_de_données",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# Exemple de requête SELECT
with conn.cursor() as cursor:
    sql = "SELECT * FROM utilisateurs"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Exemple de requête INSERT
with conn.cursor() as cursor:
    sql = "INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)"
    cursor.execute(sql, ("John Doe", "john.doe@example.com"))
    conn.commit()

# Fermeture de la connexion
conn.close()
