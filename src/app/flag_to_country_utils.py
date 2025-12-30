from pandas import DataFrame

class FlagToCountryUtils:
    def __init__(self, countries: DataFrame):
        self.countries = countries

    def get_all_countries_in_continent(self, continent = "africa") -> DataFrame:
        """Returns all countries in a specified continent. Default = Africa"""
        return self.countries.loc[self.countries.Continent == continent.lower()]

    def randomise_countries(self, countries: DataFrame) -> DataFrame:
        """Takes in a pandas DataFrame of countries and shuffles them in a random order"""
        return countries.sample(frac=1)

    def to_list(self, countries: DataFrame) -> list:
        """Returns a list of the rows in a given DataFrame"""
        result = []
        for country in countries.itertuples(index=False):
            result.append(country)

        return result

    def is_guess_correct(self, input_country: str, expected_country: str) -> bool:
        accepted_names = self.countries.loc[self.countries.CountryName == expected_country].AcceptedNames.item()
        accepted_names = accepted_names.split("#")
        for accepted_name in accepted_names:
            if input_country.lower() == accepted_name:
                return True
        return False

    def get_country_flag_path(self, country_name: str) -> str:
        """Takes in a country name and returns the path to the flag svg file"""
        country_record = self.countries.loc[self.countries.CountryName == country_name.lower()]
        if not country_record.empty:
            flag_name = country_record.FlagName.item()
            continent_name = country_record.Continent.item()
            return f"static/assets/country-flags/{continent_name}/{flag_name}.svg"
        else:
            raise FileNotFoundError(f"Cannot find flag for country: '{country_name}'")
