import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

def train_and_predict(input_path, final_output_path):
    print(f"ENTRAÎNEMENT DU MODÈLE : {input_path}")
    
    df = pd.read_csv(input_path)
    
    #Encodage
    df_encoded = pd.get_dummies(df, columns=['neighbourhood_cleansed', 'property_type', 'room_type'])
    
    #Préparation ML
    X = df_encoded.drop(columns=['id', 'is_popular', 'number_of_reviews_ltm'])
    y = df_encoded['is_popular']
    
    #Entraînement
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X, y)
    
    #Prédiction sur TOUT le dataset pour Power BI
    df['probabilite_succes'] = rf.predict_proba(X)[:, 1]
    df['probabilite_succes'] = (df['probabilite_succes'] * 100).round(1)
    
    #Export final
    df.to_csv(final_output_path, index=False)
    print(f"Fichier final prêt pour Power BI : {final_output_path}")

if __name__ == "__main__":
    CLEANED_DATA = "data/processed/listings_cleaned.csv"
    FINAL_DATA = "data/processed/airbnb_predictions_paris.csv"
    
    train_and_predict(CLEANED_DATA, FINAL_DATA)