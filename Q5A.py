def get_persons(person_list, n):
    """returns a new list of persons (tuples) in any order, in which each returned person must be enclosed by at least n different members of the opposite gender"""
    final_list = []
    count_for_male = 0
    count_for_female = 0
    # Get the number of Male and Female in the list respectively
    for each_tuple in person_list:
        if each_tuple[1] == "M":
            count_for_male += 1
        else:
            count_for_female += 1
    for index in range(len(person_list)):       # iterate through length of person_list
        current_tuple = person_list[index]
        if current_tuple == person_list[-1]:         # if at the last tuple in list
            sitted_on_right_tuple = person_list[0]   # right of last tuple is first tuple
            sitted_on_left_tuple = person_list[index - 1]
        else:                                        # for all elements (tuples) before last tuple
            sitted_on_right_tuple = person_list[index + 1]
            sitted_on_left_tuple = person_list[index - 1]
        # Need to compare current tuple with left and right tuples, check if left, right opposite gender from current
        current_tuple_gender = current_tuple[1]       # get current tuple gender
        sitted_on_right_gender = sitted_on_right_tuple[1]
        sitted_on_left_gender = sitted_on_left_tuple[1]
        # Since gender can only be 'M' or 'F', if current is M, left and right need to be F, current is F, left and right to be M
        if sitted_on_right_gender != current_tuple_gender and sitted_on_left_gender != current_tuple_gender:
            # Must also check that there is at least n number of people of opposite genders
            if current_tuple_gender == "M":
                if count_for_female == n or count_for_female > n:
                    final_list.append(current_tuple)
            else:
                if count_for_male == n or count_for_male > n:
                    final_list.append(current_tuple)
    return final_list


#print(get_persons([('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')], 2))
#print(get_persons([('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')], 3))
#print(get_persons([('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')] , 7))
#print(get_persons([('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')] , 8))