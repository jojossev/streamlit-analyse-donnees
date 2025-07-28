# Analyse Interactive de Données avec Streamlit

Une application web interactive pour analyser des fichiers CSV ou Excel. Cette application permet de visualiser des données, d'afficher des statistiques descriptives et de générer des graphiques automatiquement.

## Fonctionnalités

- Téléchargement de fichiers CSV ou Excel
- Aperçu des données
- Statistiques descriptives
- Visualisations automatiques selon le type de données
- Histogrammes pour les données numériques
- Graphiques temporels pour les dates
- Visualisation des données catégorielles

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/jojossev/streamlit-analyse-donnees.git
   cd streamlit-analyse-donnees
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application :
   ```bash
   streamlit run app.py
   ```

2. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501)

3. Téléchargez un fichier CSV ou Excel pour commencer l'analyse

## Dépendances

- streamlit
- pandas
- plotly
- openpyxl (pour la lecture des fichiers Excel)

## Licence

Ce projet est sous licence MIT.
