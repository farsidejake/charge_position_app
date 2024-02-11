import time
#t = time.localtime()
#current_time = time.strftime("%H:%M")
#print(current_time)

def get_current_time_hours():
    t = time.localtime()
    return time.strftime("H")   #returns a string

def get_current_time_minutes():
    t = time.localtime()
    return time.strftime("M")   #returns a string