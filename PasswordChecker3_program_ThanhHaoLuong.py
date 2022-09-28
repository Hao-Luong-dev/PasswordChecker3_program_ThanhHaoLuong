""""
PasswordChecker3
developed by THANH HAO LUONG
date: 29/08/2022
"""

# Pseudocode ----------------------------------------------------#
# INPUT
#        input_file = ITWorks_password_log.txt
#        count_pw_too_small = 0
#        count_pw_too_large = 0
#
# PROCESSING
#        FOR line in input_file:
#             list_data.append(line)
#        END FOR
#
#        FOR error_reason in list_data:
#              OUTPUT: error_reason
#              IF "password < 6" in error_reason"
#                   count_pw_too_small = count_pw_too_small + 1
#              ELSE
#                   count_pw_too_large = count_pw_too_large + 1
#              END IF
#
#        END FOR
# OUTPUT  count_pw_too_small
# OUTPUT  count_pw_too_large
# ----------------------------------------------------------------#

# create a function named "main"
def main():
    print("PasswordChecker3 program developed by THANH HAO LUONG")
    # variable to count error due to < 6 characters
    count_pw_too_small = 0
    # variable to count errors due to > 10 characters
    count_pw_too_large = 0

    # create an empty list to store data
    list_data = []

    # read data file "ITWorks_password_log.txt"
    input_file = open("ITWorks_password_log.txt", "r")

    # add each line of the file to the list
    for line in input_file:
        list_data.append(line)
    # close input_file
    input_file.close()

    # identify error type & count
    for error_reason in list_data:
        print(error_reason, end="")
        # if error "password <6", add 1 to count_pw_too_small, other wise add 1 to count_pw_too_large
        if "password < 6" in error_reason:
            count_pw_too_small = count_pw_too_small + 1
        # if error "password > 10", add 1 to number of error
        else:
            count_pw_too_large = count_pw_too_large + 1
    # OUTPUT
    print("number of passwords having less than 6 characters: ", count_pw_too_small)
    print("number of passwords having more than 10 characters: ", count_pw_too_large)
main()

