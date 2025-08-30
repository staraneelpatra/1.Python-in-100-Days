# def format_name(firstname, lastname):
#     fullname = (firstname+" "+lastname).title()
#     print(fullname)
#     return fullname


# fname = input('Enter your first name')
# lname = input("Enter your last name")
# print(format_name(fname, lname))
# print(len(format_name(fname,lname)))
print("------------------------------------------------------------")
def is_leap_year(year):
    """This Function take a year and returns True / False if it is a leap year"""
    # Write your code here. 
    # Don't change the function name.
    if(year % 4 == 0):
        if(year % 100 != 0):
            return True
        else:
            if(year % 400 == 0):
                return True
            else:
                return False
    else:
        return False

year = int(input("Enter year"))
isLeapYear = is_leap_year(year)
print(f"{isLeapYear} {year},Year is a leap year")
is_leap_year()