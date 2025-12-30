from pandas import DataFrame

class FlagToCountryUtils:
    def __init__(self, countries: DataFrame):
        self.countries = countries

    def get_all_countries_in_continent(self, continent = "africa") -> DataFrame:
        return self.countries.loc[self.countries.Continent == continent.lower()]

    def randomise_countries(self) -> DataFrame:
        return self.countries.sample(frac=1)

    def get_country_flag_path(self, country_name: str) -> str:
        """Takes in a country name and returns the path to the flag svg file"""
        country_record = self.countries.loc[self.countries.CountryName == country_name.lower()]
        if not country_record.empty:
            flag_name = country_record.FlagName.item()
            continent_name = country_record.Continent.item()
            return f"static/assets/country-flags/{continent_name}/{flag_name}.svg"
        else:
            raise FileNotFoundError(f"Cannot find flag for country: '{country_name}'")
