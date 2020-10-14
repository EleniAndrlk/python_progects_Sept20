import random

def check_combination(list_given):
    combination = False
    list_combination = []
    for item in list_given:
        if len(list_combination) == 0:
            list_combination.append(item)

        elif len(list_combination) == 1:
            if item != list_combination[0]:
                list_combination.clear()
                
            list_combination.append(item)

        elif len(list_combination) == 2:
            if item != list_combination[0]:
                list_combination.clear()
                
            list_combination.append(item)

        else:
            if item == list_combination[0]:
                combination = True
            list_combination.clear()
    return combination


def make_vertical_list(list_given, num_of_index_in_row):
    vertical_list = []

    for row_list in list_given:
        vertical_list.append(row_list[num_of_index_in_row])

    return vertical_list

def make_diagonal_list(list_given, index_i, index_j):
    start_index_i = index_i
    start_index_j = index_j

    left_diag_list = []
    # briskei arxiko shmeio diagoneiou apo aristera 
    while index_i != 0 and index_j != 0 :
        index_i -= 1
        index_j -= 1
        
    while index_i != start_index_i and index_j != start_index_j:
        left_diag_list.append(list_given[index_i][index_j])
        index_i += 1
        index_j += 1
    left_diag_list.append(list_given[start_index_i][start_index_j])

    index_i = start_index_i
    index_j = start_index_j
    right_diagonal_list = []
     # briskei arxiko shmeio diagoneiou apo dexia 
    while index_i != 0 and index_j != 9 :
        index_i -= 1
        index_j += 1
    while index_i != start_index_i and index_j != start_index_j:
        right_diagonal_list.append(list_given[index_i][index_j])
        index_i += 1
        index_j -= 1
        
    right_diagonal_list.append(list_given[start_index_i][start_index_j])
    
    return left_diag_list, right_diagonal_list
      
continue_fil = True

while continue_fil:

    list_row = []
    list_table = []
    choices = [0,1]
    for i in range(10):
        # list_table append row
        list_table.append([])
        for j in range(10):
            # find random choice
            choice = random.choice(choices)
            list_row.append(choice)
            # print("choice ",choice)
            list_table[i].append(choice)
            
            # check 1
            horizontal_combination = check_combination(list_row)
            if horizontal_combination:
                break
            
            vertical_list = make_vertical_list(list_table, j)
            # print("vertical list: ",vertical_list)

            # check 2
            vertical_combination = check_combination(vertical_list)
            if vertical_combination:
                break

            left_diag, right_diag = make_diagonal_list(list_table, i, j)

            # print("left_diag")
            # for m in left_diag:
            #     print(m)
            # print("right_diag")
            # for m in right_diag:
            #     print(m)
            
            #check 3 
            left_diag_combination = check_combination(left_diag)
            if left_diag_combination:
                break
            
            # check 4
            right_diag_combination = check_combination(right_diag)
            if right_diag_combination:
                break
            
        # print("row",list_row)
    
        list_row.clear()
        if horizontal_combination:
            continue_fil = False
            break
        if vertical_combination:
            continue_fil = False
            break
        if right_diag_combination:
            continue_fil = False
            break
        if left_diag_combination:
            continue_fil = False
            break



print("Horizontal Combination",horizontal_combination)
print("Vertical Combination",vertical_combination)
print("Start Left diagonally Combination",left_diag_combination)
print("Start Right diagonally Combination",right_diag_combination)

for i in list_table:
    print(i)
counter = 0
for row in list_table:
    for item in row:
        counter += 1
print("Num of rows: ",len(list_table))
print("Numbers Added to list: ",counter)




