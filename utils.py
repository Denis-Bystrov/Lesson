import json


def get_all():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_man(pk):
    people = get_all()
    maximum = len(people)
    for number in range(0, maximum):
        if people[number]["pk"] == pk:
            return people[number]


def get_candidate_by_skill(skill):
    people = get_all()
    skill = skill.title()
    maximum = len(people)
    name = []
    for i in range(0, maximum):
        if skill in people[i]["skills"]:
            name.append(people[i]["name"])
        result = ("")
        for i in range(0, len(name)):
            result += name[i]
            result += ", "
        result = result[0:len(result) - 2]
    return result


def get_candidate_by_name(name):
    people = get_all()
    maximum = len(people)
    for i in range(0, maximum):
        if name in people[i]["name"]:
            man = people[i]["name"]
    return man
