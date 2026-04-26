import pandas as pd
import os

def clean_data(input_path, output_path):
    print(f"DÉBUT DU NETTOYAGE : {input_path}")
    
    #Chargement
    df = pd.read_csv(input_path, compression='gzip', low_memory=False)
    
    #Sélection des colonnes
    colonnes = [
        'id', 'neighbourhood_cleansed', 'latitude', 'longitude', 
        'property_type', 'room_type', 'accommodates', 'bathrooms_text', 
        'bedrooms', 'beds', 'minimum_nights', 'availability_365', 
        'number_of_reviews_ltm', 'review_scores_rating'
    ]
    df = df[colonnes].copy()
    
    #Création de la cible (Target)
    df['is_popular'] = (df['number_of_reviews_ltm'] >= 12).astype(int)
    
    #Nettoyage technique
    df['bathrooms'] = df['bathrooms_text'].str.extract(r'(\d+\.?\d*)').astype(float)
    df = df.drop(columns=['bathrooms_text'])
    
    #Imputation (remplissage du vide)
    df['review_scores_rating'] = df['review_scores_rating'].fillna(df['review_scores_rating'].mean())
    for col in ['bedrooms', 'beds', 'bathrooms']:
        df[col] = df[col].fillna(1)
        
    #Sauvegarde du fichier intermédiaire
    df.to_csv(output_path, index=False)
    print(f"Nettoyage terminé. Fichier sauvegardé : {output_path}")

if __name__ == "__main__":
    #On définit les chemins
    RAW_DATA = "data/raw/listings.csv.gz"
    PROCESSED_DATA = "data/processed/listings_cleaned.csv"
    
    #On crée le dossier processed 
    os.makedirs("data/processed", exist_ok=True)
    
    clean_data(RAW_DATA, PROCESSED_DATA)