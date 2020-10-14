# 1.a
import random
# import numpy as np


table = []

# sinartisi dexetai san orisma to megethos tou tetragonikou pinaka
# kai ton dimiourgei
def create_table(m=10):
    list_row = []
    list_table = []
    choices = ['S','O']
    for i in range(10):
       
        for j in range(10):
            list_row.append(random.choice(choices))
        # print("row",list_row)
        table.append(list_row[:])
        list_row.clear()


def count_sos(list_given):
    counter = 0
    list_combination = []
    for item in list_given:
        if len(list_combination) == 0:
            if item == 'S':
                list_combination.append(item)

        elif len(list_combination) == 1:
            if item == 'S':
                list_combination.clear()

            list_combination.append(item)

        else:
            list_combination.clear()
            if item == 'S':
                counter +=1
                # ginetai prosthiki stin lista to teleutaio S giati mporei na anhkei kai se epomeno px SOSOS
                list_combination.append(item)

        
    list_combination.clear()
    return counter


def make_vertical_list(list_given, num_of_index_in_row):
    vertical_list = []

    for row_list in list_given:
        vertical_list.append(row_list[num_of_index_in_row])

    return vertical_list


def make_diagonal_lists():
    max_col = len(table[0])
    max_row = len(table)
    fdiag = [[]for _ in range(max_row +max_col - 1)]
    bdiag =[[] for _ in range(len(fdiag))]
    min_bdiag = -max_row +1
    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(table[y][x])
            bdiag[x-y-min_bdiag].append(table[y][x])

    return fdiag, bdiag




create_table()
print("Random table")
for i in table:
    print(i)


horizontally_counter = 0
for row in table:
    horizontally_counter += count_sos(row)
print("Horizontally count of SOS: ",horizontally_counter)

vertically_counter = 0
for i in range(10):
    list_vert = make_vertical_list(table, i)
    vertically_counter += count_sos(list_vert)

print("Vertically count of SOS: ",vertically_counter)

diagonally_counter = 0
fdiag, bdiag = make_diagonal_lists()
for list_diag in fdiag:
    diagonally_counter += count_sos(list_diag)
for list_diag in bdiag:
    diagonally_counter += count_sos(list_diag)


print("Diagonally count of SOS: ",diagonally_counter)

