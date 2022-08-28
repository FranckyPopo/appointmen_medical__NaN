def format_date_appointment(date_string: str) -> str:
    day = month = year = None
    day = date_string[3:5]
    month = date_string[0:2]
    year = date_string[6:]
    print(day, month, year)
    return f"{day}/{month}/{year}"
    
    
     