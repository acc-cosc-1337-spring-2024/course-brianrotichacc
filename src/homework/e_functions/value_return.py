
def get_hour(sec):
    hours_since_1970 = sec//3600
    current_hour = hours_since_1970 % 24
    return current_hour

def get_minutes(sec):
    minutes_since_1970 = sec//60
    current_minute = minutes_since_1970 % 60
    return current_minute

def get_seconds(sec):
    current_second = sec % 60
    return current_second