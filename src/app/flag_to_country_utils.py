from pandas import DataFrame, read_csv

df = read_csv("../static/data/countries.csv")

def get_all_countries_in_continent(continent = "africa") -> DataFrame:
    return df.loc[df.Continent == continent.lower()]

print(get_all_countries_in_continent("Europe"))
print(df.to_json())