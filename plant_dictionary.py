import pandas as pd
import wikipedia

def get_plant_info(name, csv_file="data/indian_authentic_250_crops.csv"):
    df = pd.read_csv(csv_file)
    match = df[df["PlantName"].str.lower() == name.lower()]
    if not match.empty:
        return match.iloc[0]["Description"]
    else:
        try:
            return wikipedia.summary(name, sentences=2, auto_suggest=True, redirect=True)
        except:
            return "No information found."
