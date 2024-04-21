import importlib
import json
import _csv as csv


def read_from_csv(file_path):
    data = []
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter='\n', quotechar='|')
        for row in reader:
            data.append(row[0])
    return data


def main():
    constants = read_from_csv('csv/constants.csv')
    objects = read_from_csv('csv/objects.csv')

    questions = []

    for i in range(len(objects)):
        question = objects[i]
        for c in range(len(constants)):
            questions.append("Return " + question + ' ' + constants[c])

    testarr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chararr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(8):
        module_name = f"algorithms.{i}"
        module = importlib.import_module(module_name)
        print(module.run(testarr))
        print(module.run(chararr))

    print(questions)
    return questions


__main__ = main()
