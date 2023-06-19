# Utilise une image de base avec Python préinstallé
FROM python:3.9

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
#COPY requirements.txt .

# Installe les dépendances Python spécifiées dans requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Copie tous les fichiers du répertoire local dans le conteneur
COPY . .

# Expose le port sur lequel le serveur web écoute
EXPOSE 8000

# Commande pour exécuter l'application lorsque le conteneur démarre
CMD ["python", "app.py"]
