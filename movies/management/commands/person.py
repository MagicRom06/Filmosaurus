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
