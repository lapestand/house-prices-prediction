import os
import pandas as pd


all_data = list()

for file_name in os.listdir("real_estate_scraper"):
    if file_name.endswith(".csv"):
        data = pd.read_csv(os.path.join("real_estate_scraper", file_name), dtype="unicode")
        print(f"File name -> {file_name}\tdataset len -> {len(data)}")
        all_data.append(data)

houses = pd.concat(all_data)
houses = houses.drop_duplicates()

houses.to_csv("dataset.csv")
