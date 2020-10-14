import random

def find_reversed(number_ran):

    num_random = str(number_ran)
    number_digits_list = []
    for digit in num_random:
        number_digits_list.append(digit)

    reversed_number_str = ""

    for i in range(len(number_digits_list)-1,-1,-1):
        reversed_number_str += number_digits_list[i]

    reversed_number = int(reversed_number_str)

    return reversed_number

# continue until value is acceptable
unacceptable = True
while unacceptable:

    print("Random integer from 1 to 1000")
    num1 = random.randint(1, 1000)
    print("Random integer: ", num1)

    if num1 != 196 and num1!= 879 :
        #value is acceptable
        unacceptable = False

palindromos = False
while not palindromos:

    reversed_number = find_reversed(num1)
    print("Reversed Integer: ",reversed_number)

    add = num1 + reversed_number
    print("Addition of the numbers: ",add)
    # reverse add
    reverse_addition = find_reversed(add)
    if reverse_addition == add:
        palindromos = True
    else:
        num1 = add

