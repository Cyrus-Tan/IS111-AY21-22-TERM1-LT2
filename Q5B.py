import itertools
from Q5A import get_persons          # import function from Q5A

def get_seating(person_list, n, m):
    final_seating = []
    all_sequences = itertools.permutations(person_list)    # find all possible arrangements
    for sequence in all_sequences:
        list_for_each_sequence = list(sequence)
        # Find the possible list where person enclosed by at least n number of opposite gender
        list_enclosed_by_n = get_persons(person_list=list_for_each_sequence, n=n)
        count_for_male = 0
        count_for_female = 0
        for each_tuple in list_enclosed_by_n:    # check how many people "M" or "F" in the list output from Q5A
            if each_tuple[1] == 'M':
                count_for_male += 1
            elif each_tuple[1] == 'F':
                count_for_female += 1
            if count_for_male == m or count_for_male > m:
                if len(final_seating) == 0:                  # only add arrangement to the list if its currently empty
                    final_seating.append(sequence)
            if count_for_female == m or count_for_female > m:
                if len(final_seating) == 0:
                    final_seating.append(sequence)
    return final_seating

#print(get_seating([('john', 'M'), ('val', 'F'), ('ann', 'F'), ('alex', 'F'), ('don', 'M')], 3, 2))
#print(get_seating([('john', 'M'), ('val', 'F'), ('ann', 'F'), ('alex', 'F'), ('don', 'M')], 3, 3))
#print(get_seating([('john', 'M'), ('val', 'F'), ('ann', 'F'), ('don', 'M'), ('alex', 'F')], 3, 2))
print(get_seating([('a', 'M'), ('b', 'M'), ('c', 'M'), ('d', 'M'), ('e', 'F'), ('f', 'F'), ('g', 'F'), ('h', 'F')] , 4, 2))