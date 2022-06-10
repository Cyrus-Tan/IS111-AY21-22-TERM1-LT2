def read_schedule(filename):
    final_dict = {}

    data = open('schedule1.txt')          # open text file
    for line in data:
        line = line.rstrip()                        # remove \n at the end of each line
        line_as_list = line.split("|")              # split into a list of strings
        day = line_as_list[0]
        workers_name = line_as_list[-1]
        list_of_workers_name = workers_name.split(" ")  # split those separated by whitespace
        start_time_list = list(line_as_list[1])
        starting_time_as_string = ""
        end_time_list = list(line_as_list[2])
        ending_time_as_string = ""
        # To convert time to int in 24h format (for starting time)
        for char in start_time_list:
            if char.isnumeric() == True:   # if its a number
                starting_time_as_string += char
                starting_time_as_int = int(starting_time_as_string)
                if start_time_list[-2] == "A":    # if its AM, number remains same
                    starting_time_as_int += 0
                elif start_time_list[-2] == "P" and starting_time_as_int == 12:  # if its 12PM
                    starting_time_as_int += 0                                    # will remain same
                else:
                    starting_time_as_int += 12      # convert time to 24h format
        # To convert time to int in 24h format (for ending time)
        for char in end_time_list:
            if char.isnumeric() == True:    # if its a number
                ending_time_as_string += char
                ending_time_as_int = int(ending_time_as_string)
                if end_time_list[-2] == "A":     # if its AM, number remains
                    ending_time_as_int += 0
                elif end_time_list[-2] == "P" and ending_time_as_int == 12:    # if its 12PM, remain same
                    ending_time_as_int += 0
                else:
                    ending_time_as_int += 12          # convert time to 24h format
        current_time_difference = ending_time_as_int - starting_time_as_int
        # To iterate through each worker name

        for name in list_of_workers_name:                                   # iterate through each name for each line
            tuple_value = (starting_time_as_int, ending_time_as_int, name)
            if day not in final_dict:                                       # if its a new day
                final_dict[day] = [tuple_value]
            else:                                                           # if day is existing
                for each_list in list(final_dict.values()):         # convert the dict values into a list, iterate through the list
                    for each_tuple in each_list:                    # iterate through each tuple
                        if name not in each_tuple:                                      # check if name not existing yet
                            final_dict[day].append(tuple_value)                         # add tuple_value to the existing list
                        elif name in each_tuple:                                        # if name exists---> To compare the values(diff in hours)
                            previous_time_difference = each_tuple[1] - each_tuple[0]
                            # If current timeslot lower or same as previous timeslot for same person on same day: will replace that slot
                            if current_time_difference < previous_time_difference or current_time_difference == previous_time_difference:
                                # Need to convert the previous tuple to a list, then change its elements(start and end time) to the new one, then convert back to tuple
                                previous_timeslot_as_list = list(each_tuple)
                                previous_timeslot_as_list[0] = starting_time_as_int     # change starting time to new one
                                previous_timeslot_as_list[1] = ending_time_as_int       # change ending time to new one
                                each_tuple = tuple(previous_timeslot_as_list)
    return final_dict


print(read_schedule('schedule1.txt'))
# LEFTOVER ISSUE: need to compare the hours for each name for each day
# No repeated names, only lowest diff in number will be shown, if same hours--> last entry will be shown
# Can't get new_tuple to replace the old tuple each_tuple ----> How to replace tuple in a list, which are the value of dictionary