from movies.models import Country


class CountryToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(countries_list):
        for country in countries_list:
            Country.objects.create(
                name=country
            )
