def get_tuples_of_size(tup_list, num):
    final_list = []
    for tuple_nums in tup_list:
        length_of_tuple_nums = len(tuple_nums)
        if length_of_tuple_nums == num or length_of_tuple_nums > num:   # if have num or more elements
            final_list.append(tuple_nums)
    return final_list


#print(get_tuples_of_size([(1, -1, 18), (4, 2, 6), (19, 0)], 3))
#print(get_tuples_of_size([(1, 2, 0), (4, 20)], 1))
#print(get_tuples_of_size([(1, 2), (9, 6), (-9, 2)], 4))
print(get_tuples_of_size([], 1))