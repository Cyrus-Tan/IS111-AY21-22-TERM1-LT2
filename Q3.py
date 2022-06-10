import datetime
def get_days_between(start_tup, end_tup):
    """returns number of days diff between two dates in the form (year, month, day)"""
    start_date = datetime.date(*start_tup)      # * unpacks the tuple
    end_date = datetime.date(*end_tup)
    return (end_date - start_date).days

def get_vaccination_status(filename, today):
    """returns a Python dictionary storing the vaccination statuses of all persons listed in the file. In the dictionary, each key is a person identification string, while the corresponding value is a tuple in the form of (age, vaccinated)"""
    final_dict = {}
    data = open(filename)                # use open() to open a text file, YOU CAN'T IMPORT text file
    for line in data:
        line = line.rstrip()                # TAKE NOTE: Currently, each line in data has "\n" at the end---> thus giving the empty lines between  ( Use .rstrip() to remove '\n'), don't need state '\n'
        splitted_line = line.split("|")     # split each line separated by pipe char(|) into a list of strings
        identification_string = splitted_line[0]      # get first element in list
        age_as_int = int(splitted_line[1])            # get person's age as int
        first_date = splitted_line[2]
        second_date = splitted_line[3]
        # Check for age < 12, will be unvaccinated
        if age_as_int < 12:
            final_dict[identification_string] = (age_as_int, False)     # Create a dict of key(identification_string) and pair(tuple of age and boolean if is vaccinated)
        # Need change first and second date from date/month/year format to a tuple of (year,month,date) format
        elif first_date == "NA" or second_date == "NA":                 # if not both doses given, is unvaccinated
            final_dict[identification_string] = (age_as_int, False)
        else:
            list_as_date_month_year = first_date.split("/")       # Split string into a list of date, month, year
            temporary_variable = int(list_as_date_month_year[0])           # Store first element date as temporary variable
            list_as_date_month_year[0] = int(list_as_date_month_year[-1])  # first element will now be year
            list_as_date_month_year[-1] = temporary_variable               # last element will now be date
            list_as_date_month_year[1] = int(list_as_date_month_year[1])
            first_date_formatted_tuple = tuple(list_as_date_month_year)     # convert to a tuple of (year,month,date)
            list_as_date_month_year_second = second_date.split("/")
            temporary_variable_second = int(list_as_date_month_year_second[0])
            list_as_date_month_year_second[0] = int(list_as_date_month_year_second[-1])
            list_as_date_month_year_second[-1] = temporary_variable_second
            list_as_date_month_year_second[1] = int(list_as_date_month_year_second[1])
            second_date_formatted_tuple = tuple(list_as_date_month_year_second)

            # Format today from string of date/month/year to tuple of (year,month,date)
            list_today = today.split("/")
            temporary_variable_third = int(list_today[0])
            list_today[0] = int(list_today[-1])
            list_today[-1] = temporary_variable_third
            list_today[1] = int(list_today[1])
            today_date_formatted_tuple = tuple(list_today)

            number_of_days = get_days_between(start_tup=first_date_formatted_tuple, end_tup=second_date_formatted_tuple)
            number_of_days_second_dose_to_today = get_days_between(start_tup=second_date_formatted_tuple, end_tup=today_date_formatted_tuple)
            if number_of_days < 28 or number_of_days > 56:      # if second dose given less than 28 days or more than 56 days after first dose
                final_dict[identification_string] = (age_as_int, False)
            elif number_of_days_second_dose_to_today < 14:      # second dose less than 14 days from today
                final_dict[identification_string] = (age_as_int, False)
            else:
                final_dict[identification_string] = (age_as_int, True)
    return final_dict


#print(get_vaccination_status('record1.txt', '25/10/2021'))
#print(get_vaccination_status('record1.txt', '15/11/2021'))
#print(get_vaccination_status('record1.txt', '15/1/2021'))