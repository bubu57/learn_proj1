from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base_de_donnees"
)

# Définition d'une route pour afficher les informations de la base de données
@app.route('/')
def afficher_infos_db():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM votre_table")
    resultats = cursor.fetchall()
    return render_template('index.html', resultats=resultats)

if __name__ == '__main__':
    app.run(debug=True)
