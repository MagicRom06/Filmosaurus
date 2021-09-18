from movies.models import Country


class CountryToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(countries_list):
        for country in countries_list:
            if Country.objects.filter(name=country).exists():
                print(f"{country} exists")
            else:
                print(f"{country} not exists")
                Country.objects.create(
                    name=country
                )
