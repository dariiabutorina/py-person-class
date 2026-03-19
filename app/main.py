class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife = (
                Person.people)[human["wife"]]
            Person.people[human["wife"]].husband = (
                Person.people)[human["name"]]

        if human.get("husband") is not None:
            Person.people[human["name"]].husband = (
                Person.people)[human["husband"]]
            Person.people[human["husband"]].wife = (
                Person.people)[human["name"]]

    return person_list
