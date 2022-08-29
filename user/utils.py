import datetime

def format_date_appointment(date_string: str) -> datetime.date:
    """Cette fonction formate date_string en le format suivant: day/mm/year
    et nous retourne un object date"""
    
    day = month = year = None
    day = int(date_string[3:5])
    month = int(date_string[0:2])
    year = int(date_string[6:])
    return datetime.date(year, month, day)
    
    
     