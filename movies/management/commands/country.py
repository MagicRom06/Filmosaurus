from movies.models import Country


class CountryToDB:
    """
    class used for insert
    Cointries on DB
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(countries_list):
        """
        Check if the country already exists in DB
        if not => insert it
        """
        for country in countries_list:
            if Country.objects.filter(name=country).exists():
                print(f"{country} exists")
            else:
                print(f"{country} not exists")
                Country.objects.create(
                    name=country
                )
