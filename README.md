# Airbnb Decision Intelligence - Paris

## Présentation du Projet
Ce projet est un outil d'aide à la décision pour les investisseurs immobiliers souhaitant se lancer sur le marché Airbnb à Paris. 

L'objectif est de dépasser la simple analyse descriptive en utilisant le **Machine Learning** pour prédire le succès (popularité) d'un futur logement en fonction de ses caractéristiques (quartier, type de bien, nombre de chambres, etc.).

##  Pipeline Technique
Le projet suit une architecture modulaire pour assurer l'industrialisation des données :

1.  **Extraction & Nettoyage (`src/data_cleaning.py`)** : Traitement des données brutes d'Inside Airbnb, gestion des valeurs manquantes et feature engineering.
2.  **Modélisation IA (`src/model_training.py`)** : Entraînement d'un modèle **Random Forest** (Précision : **84.39%**) pour classifier les logements "Top Performers".
3.  **Visualisation (Power BI)** : Dashboard interactif pour explorer les zones à fort potentiel.

## Intelligence Artificielle
Suite à une indisponibilité des données de prix sur l'extraction actuelle, le projet a pivoté sur la prédiction de la **popularité** (basée sur le flux de commentaires des 12 derniers mois). 

**Top 3 des facteurs de succès identifiés par l'IA :**
* **Note globale (`review_scores_rating`)** : L'expérience client est le levier n°1.
* **Disponibilité (`availability_365`)** : Corrélation forte entre succès et taux d'occupation.
* **Localisation (`latitude`)** : Importance cruciale du positionnement géographique dans Paris.

## Installation et Utilisation
```bash
# Initialiser l'environnement
pip install -r requirements.txt

# Lancer le pipeline complet
python src/data_cleaning.py
python src/model_training.py