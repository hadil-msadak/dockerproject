# Utilisez une image Python comme base
FROM python:3.8-slim

# Créez le répertoire de travail et copiez les fichiers nécessaires
WORKDIR /app
COPY . /app

# Installez les dépendances
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.py

# Exposez le port sur lequel Flask va écouter
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "app/main.py"]
