from movies.models import Person


class PersonToDB:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def insert(person_list):
        for person in person_list:
            if Person.objects.filter(name=person).exists():
                print(f'{person} Person exists')
            else:
                print(f'{person} Not exists')
                Person.objects.create(
                    name=person
                )
