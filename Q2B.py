def extract_names_2(name_list):
    final_list = []
    count_alphabet = 0
    individual_name = ""
    for name in name_list:
        for char in name:
            if char.isalpha() == True or char == " ":     # if char in name is alphabet or whitespace
                individual_name += char
            if char.isalpha() == True:
                count_alphabet += 1                       # keep track of how many alphabets there are in each string
        if count_alphabet == 0:
            pass                                          # if string has no alphabets, then don't add the string
        else:
            final_list.append(individual_name)                # when done for every char in each name
            individual_name = " "                     # reset individual_name so that can add next name into it
            count_alphabet = 0                        # reset count_alphabet so i can count again afterwards
    return final_list


#print(extract_names_2(['Alex T5an', '^Harry Potter$', 'Squid$$ Game', 'abc','5 -6- 7-8']))
#print(extract_names_2(['Alina Star**kov', 'Jessie Mei   Li']))
#print(extract_names_2(['@@ 12']))
#print(extract_names_2([]))