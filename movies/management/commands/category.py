from movies.models import Category


class CategoryToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(categories_list):
        for category in categories_list:
            Category.objects.create(
                name=category
            )

    @staticmethod
    def is_empty():
        try:
            Category.objects.all()[0]
            return False
        except IndexError:
            return True
