def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                leap = True
            else:
                print("Not leap year.")
                leap = False
        else:
            print("Leap year.")
            leap = True
    else:
        print("Not leap year.")
        leap = False
    return leap

def days_in_month(year, month):
    if month > 12 or month < 12:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if is_leap(year):
            month_days[1] = 29
    return month_days[month - 1]


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












