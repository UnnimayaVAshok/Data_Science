# count uppercase,lowercase,digits and special characters

# text = "ProgramMING@123"

def count(text):

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_others = 0

    for i in text:

        if i.islower() == True:

            count_lower += 1

        elif i.isupper() == True:

            count_upper += 1

        elif i.isdigit() == True:

            count_digit += 1

        else:

            count_others += 1

    return count_lower,count_upper,count_digit,count_others

print(count("ProgramMING@123"))