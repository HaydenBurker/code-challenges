# Create a function that converts a date format from MM/DD/YYYY to YYYYMMDD

def date_format(date_str):
    month, day, year = date_str.split("/")
    return f'{year}{month}{day}'

print(date_format("09/27/2024")) # "20240927"
print(date_format("01/01/2001")) # "20010101"
print(date_format("12/31/2022")) # "20221231"