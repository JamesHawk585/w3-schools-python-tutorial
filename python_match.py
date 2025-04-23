day = 10
match day: 
    case 1: 
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4: 
        print("Thursday")
    case _:
        print("Default value used.")


weekday = 1
match weekday: 
    case 1 | 2| 3| 4| 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


# You can add if statements in the case evaluation as an extra condition-check:

month = 5
day_of_week = 4
match day_of_week:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4| 5 if month ==5:
        print("A weekday in May")
    case _:
        print("No match.")

my_month = 12
my_day = 12


    