def extract_names_1(str_name):
    final_list = []
    splitted_string = str_name.split("#")    # get a list of strings separated by '#'
    for string in splitted_string:
        if string != "":                     # if string is not empty, add to final_list
            final_list.append(string)
    return final_list


#print(extract_names_1('Alex Tan##xy1 z####abc$#S'))
#print(extract_names_1('ab c#def'))