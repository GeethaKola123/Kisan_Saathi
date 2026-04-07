import pandas as pd

def recommend_fertilizer(soil_type, crop, prev_crop, fert_file="data/icar_fertilizer.csv"):
    fert_df = pd.read_csv(fert_file)
    match = fert_df[(fert_df["Crop"].str.lower() == crop.lower()) & 
                    (fert_df["SoilType"].str.lower() == soil_type.lower())]
    if not match.empty:
        return match.iloc[0]["Recommendation"]
    else:
        return f"Use balanced NPK fertilizer for {crop} after {prev_crop} in {soil_type} soil."
