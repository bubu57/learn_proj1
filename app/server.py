from flask import Flask, render_template
import psycopg2  # Remplacez psycopg2 par le connecteur adapté à votre base de données

app = Flask(__name__)

# Configuration de la base de données
DB_HOST = 'localhost'
DB_NAME = 'votre_base_de_donnees'
DB_USER = 'votre_utilisateur'
DB_PASSWORD = 'votre_mot_de_passe'

# Fonction pour se connecter à la base de données
def connect_to_database():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        return conn
    except Exception as e:
        print("Erreur lors de la connexion à la base de données:", e)

# Route pour afficher les informations de la base de données
@app.route('/')
def display_db_info():
    try:
        # Se connecter à la base de données
        conn = connect_to_database()
        cursor = conn.cursor()

        # Exemple de requête SQL pour récupérer des données
        cursor.execute("SELECT * FROM votre_table;")
        data = cursor.fetchall()

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        # Renvoyer les données à afficher dans le template HTML
        return render_template('index.html', data=data)
    except Exception as e:
        print("Erreur lors de la récupération des données de la base de données:", e)
        return "Erreur lors de la récupération des données de la base de données"

if __name__ == '__main__':
    app.run(debug=True)
