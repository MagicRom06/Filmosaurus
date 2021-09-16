from movies.models import Person


class PersonToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(person_list):
        for person in person_list:
            Person.objects.create(
                name=person
            )

    @staticmethod
    def is_empty():
        try:
            Person.objects.all()[0]
            return False
        except IndexError:
            return True
