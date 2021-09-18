from movies.models import Country


class CountryToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(countries_list):
        for country in countries_list:
            print(country)
            Country.objects.create(
                name=country
            )

    @staticmethod
    def is_empty():
        try:
            Country.objects.all()[0]
            return False
        except IndexError:
            return True
