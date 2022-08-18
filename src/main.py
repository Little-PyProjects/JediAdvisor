import os
from random import sample

def enum_sayings(file):
    with open (file) as f:
        for (num, saying) in enumerate(f):
            return num, saying


def get_line_count(file)->int :
    '''
    Calculates the number of lines in file.
    '''
 
    with open(file) as f:
        line_count = sum(1 for _ in f)
    return line_count


def gen_order (line_count: int):
    print(f'the number of lines is {line_count}')

    indexes = [i for i in range(line_count)]
    order = sample(indexes, len(indexes))
    print (order)




if __name__ == "__main__":
    file = ('../data/CloneWarsSayings.txt')

    line_count = get_line_count(file)
    gen_order(line_count)
