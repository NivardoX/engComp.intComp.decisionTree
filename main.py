from copy import copy
from pprint import pprint

import math


def calculate_entropia(values):
    c_true = values.count(True) / len(values)
    c_false = values.count(False) / len(values)
    if not c_true or not c_false:
        return 0
    return -c_true * math.log(c_true, 2) - c_false * math.log(c_false, 2)


def decision_tree(dataset, level=0):
    copy_dataset = copy(dataset)
    if len(dataset) < 1 or len(dataset[0]) < 3:
        return -1
    dataset = list(map(list, zip(*dataset)))
    I = calculate_entropia(dataset[-1][1:])

    if I == 0:
        print(''.join(['\t' for _ in range(level+1)]), 'Result:', dataset[-1][1])
        return
    attributes = dataset[1:-1]

    average_i = []
    for attribute in attributes:
        visited = []
        Im = 0
        for attribute_value in attribute[1:]:
            values = []
            if attribute_value not in visited:
                for j, attribute_value_aux in enumerate(attribute[1:]):
                    if attribute_value == attribute_value_aux:
                        values.append(dataset[-1][j+1])
                visited.append(attribute_value)
                Im += attribute.count(attribute_value)/len(attribute[1:]) * calculate_entropia(values)
        average_i.append(Im)
    max_i = 0
    chose = 0
    for i, Im in enumerate(average_i):
        if max_i < I - Im:
            max_i = I - Im
            chose = i
    print(''.join(['\t' for _ in range(level)]), dataset[chose+1][0], level)
    visited = []
    for attribute_value in dataset[chose+1][1:]:
        if attribute_value not in visited:
            print(''.join(['\t' for _ in range(level)]), '-->', attribute_value)
            filtered_dataset = [[]]
            count = 0
            for i, line in enumerate(copy_dataset):
                if i == 0 or attribute_value in line:
                    for j, collumn in enumerate(line):
                        if j != chose+1:
                            filtered_dataset[count].append(collumn)
                    filtered_dataset.append([])
                    count += 1
            filtered_dataset = filtered_dataset[0: -1]
            visited.append(attribute_value)
            decision_tree(filtered_dataset, level+1)

    return


if __name__ == '__main__':
    
    dataset = [
        ['N', 'Tempo', 'Temperatura', 'Humidade', 'Ventando', 'Foi jogar?'],
        [1, 'Ensolarado', 'Quente', 'Alta', 'Sim', False],
        [2, 'Ensolarado', 'Quente', 'Alta', 'Sim', False],
        [3, 'Nublado', 'Quente', 'Alta', 'N??o', True],
        [4, 'Chuva', 'M??dia', 'Alta', 'N??o', True],
        [5, 'Chuva', 'Fria', 'Normal', 'N??o', True],
        [6, 'Chuva', 'Fria', 'Normal', 'Sim', False],
        [7, 'Nublado', 'Fria', 'Normal', 'Sim', True],
        [8, 'Ensolarado', 'M??dia', 'Alta', 'N??o', False],
        [9, 'Ensolarado', 'Fria', 'Normal', 'N??o', True],
        [10, 'Chuva', 'M??dia', 'Normal', 'N??o', True],
        [11, 'Ensolarado', 'M??dia', 'Normal', 'Sim', True],
        [12, 'Nublado', 'M??dia', 'Alta', 'Sim', True],
        [13, 'Nublado', 'Quente', 'Normal', 'N??o', True],
        [14, 'Chuva', 'M??dia', 'Alta', 'Sim', False],
    ]

    print("Dataset: ")
    pprint(dataset)
    print("Decision tree:")
    decision_tree(dataset)