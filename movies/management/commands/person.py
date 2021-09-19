from movies.models import Person


class PersonToDB:
    """
    class used for insert
    Persons on DB
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(person_list):
        """
        Check if the person already exists in DB
        if not => insert it
        """
        for person in person_list:
            if Person.objects.filter(name=person).exists():
                print(f'{person} Person exists')
            else:
                print(f'{person} Not exists')
                Person.objects.create(
                    name=person
                )
