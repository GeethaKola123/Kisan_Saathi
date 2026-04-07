import pandas as pd

def predict_crop(weather, location, soil_type, prev_crop, soil_atlas_file="data/soil_atlas.csv"):
    soil_df = pd.read_csv(soil_atlas_file)
    district_soil = soil_df[(soil_df["State"] == location["state"]) & 
                            (soil_df["District"] == location["district"])]
    
    # Dummy rule-based logic (replace with ML if you want)
    if weather["rainfall"] > 200 and soil_type.lower() == "clay":
        return "Rice"
    elif weather["temperature"] > 30 and soil_type.lower() == "sandy":
        return "Millets"
    else:
        return "Wheat"
