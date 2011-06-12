class Time:
    """This class is an object to represent
    time with variables hours minutes and seconds"""
    
    
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    
def add_time(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    while sum.seconds > 60:
        sum.seconds = sum.seconds - 60
        sum.minutes = sum.minutes + 1
    while sum.minutes > 60:
        sum.minutes = sum.minutes - 60
        sum.hours = sum.hours + 1
    while sum.hours > 24:
        sum.hours = sum.hours - 24

    return sum

def convert_to_seconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds


def make_time(seconds):
    time = Time()
    time.hours = seconds/3600
    seconds = seconds - time.hours * 3600
    time.minutes = seconds/60
    time.seconds = seconds - time.minutes * 60
    return time

def increment(time, seconds):
    new_time = Time()
    new_time = convert_to_seconds(time) + seconds
    new_time = make_time(new_time)
    return new_time

def add_time2(t1, t2):
    seconds = convert_to_seconds(t1) + convert_to_seconds(t2)
    return make_time(seconds)


def print_time(t):
    print("%s:%s:%s") % (t.hours, t.minutes, t.seconds)


def after(t1, t2):
    if convert_to_seconds(t1) > convert_to_seconds(t2):
        return True
    else:
        return False



