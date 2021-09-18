from movies.models import Category


class CategoryToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(categories_list):
        for category in categories_list:
            if Category.objects.filter(name=category).exists():
                print(f"{category} exists")
            else:
                print(f"{category} not exists")
                Category.objects.create(
                    name=category
                )
