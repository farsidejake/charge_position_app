#import time
from datetime import datetime, timedelta
#t = time.localtime()
#current_time = time.strftime("%H:%M")
#print(current_time)




def get_current_time():
    # t = time.localtime()
    # current_time = time.strftime("%H:%M")
    # return current_time

    current_time = datetime.now().strftime('%H:%M')
    return current_time
    #return '00:30'

def find_closest_time(time_list):
    current_time = datetime.strptime(get_current_time(), '%H:%M')
    time_list = [datetime.strptime(time, '%H:%M') for time in time_list]

    past_times = [time for time in time_list if time < current_time]

    if not past_times:
        last_time = max(time_list)
        return last_time.strftime('%H:%M')

    most_recent = max(past_times)

    if most_recent < current_time - timedelta(days=1):
        # If the most recent time is from the previous day, we need to find the closest time from yesterday
        past_times = [time for time in time_list if time > current_time - timedelta(days=1)]
        most_recent = max(past_times)

    last_charge = most_recent.strftime('%H:%M')
    
    return last_charge


def charge_time(push):
    #time list 24 hour time for each charge
    #rate is duration between charges in hours
    
    match push:
        #i should also do lists for 4 car push and 5 car push, we do go that slow occasionally.

        case 6:
            times = ['02:00', '06:00', '10:00', '14:00', '18:00', '22:00']
            rate = 24 / 6
        case 7:
            times = ['01:26', '04:52', '08:18', '11:44', '15:10', '18:36', '22:00']
            rate = 24 / 7
        case 8:
            times = ['00:30', '03:30', '06:30', '09:30', '12:30', '15:30', '18:30', '21:30']
            rate = 24 / 8
        case 9:
            times = ['00:30', '03:10', '05:50', '08:30', '11:10', '13:50', '16:30', '19:10', '21:50']
            rate = 24 / 9
        case 10:
            times = ['00:14', '02:38', '05:02', '07:26', '09:50', '12:14', '14:38', '17:02', '19:26', '21:50']
            rate = 24 / 10
        case 11:
            times = ['00:48', '02:59', '05:10', '07:20', '09:31', '11:42', '13:53', '16:04', '18:15', '20:26', '22:37']
            rate = 24 / 11
        case 12:
            times = ['00:15', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00']
            rate = 24 / 12
        case 13:
            times = ['01:45', '03:40', '05:30', '07:20', '09:10', '11:00', '12:50', '14:40', '16:30', '18:20', '20:10', '22:00', '23:50']
            rate = 24 / 13
        case 14:
            times = ['00:33', '02:16', '04:00', '05:43', '07:20', '09:03', '10:46', '12:30', '14:13', '15:56', '17:40', '19:23', '21:05', '22:50']
            rate = 24 / 14
    return times, rate

def number_crunch(rate, last_charge, current_time):
    current_time = datetime.strptime(current_time, '%H:%M')
    last_charge = datetime.strptime(last_charge, '%H:%M')

    time_diff = current_time - last_charge 
    time_diff_minutes = time_diff.seconds // 60

    inches_minute = 120 / (rate * 60)
    current_position = time_diff_minutes * inches_minute
    return current_position


def main():
    push = 7


    ## testing code     
    # print(get_current_time())
    
    # times, rate = charge_time(push)
    # print(times)
    # print(rate)

    # # times = ['09:00', '11:25', '12:30', '15:45', '18:20', '21:00']
    # closest_time = find_closest_time(times)
    # print("Closest time:", closest_time)

    #END Testing Code


    #### ------------------- ####
    ## this starts actual main section

    times, rate = charge_time(push)
    distance = number_crunch(rate, find_closest_time(times), get_current_time())

    print(distance)
    return None

if __name__ == '__main__':
    main()