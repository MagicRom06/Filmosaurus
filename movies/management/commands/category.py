from movies.models import Category


class CategoryToDB:
    """
    class used for insert
    Categories on DB
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(categories_list):
        """
        Check if the category already exists in DB
        if not => insert it
        """
        for category in categories_list:
            if Category.objects.filter(name=category).exists():
                print(f"{category} exists")
            else:
                print(f"{category} not exists")
                Category.objects.create(
                    name=category
                )
