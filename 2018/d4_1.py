""" --- Day 4: Repose Record part 1---"""

import sys

class Record():
    
    def __init__(self, date, hour, mn, action = "", id_g=None):
        self.date = date
        self.hour = hour
        self.mn = mn
        self.action = action
        self.id_g = id_g 



def get_lazzy_guard(records, guards):
    i = 0
    guard = None
    max_guard = None
    max_sleep_time = 0
    max_min_sl = 0
    sleep_time = 0

    while i < len(records):
        r = records[i]

        if r.action == "G":
            guard = r.id_g
            i += 1
            continue

        mn_sl= int(r.mn)
        mn_aw = int(records[i+1].mn)
        clock = guards[guard]["clock"]
        if mn_sl > mn_aw:
            sleep_time = 60 - mn_sl + mn_aw
            clock[60 - mn_sl:] = [m + 1 for m in clock[60 - mn_sl:]]
            clock[:mn_aw] = [m + 1 for m in clock[:mn_aw]]
        else:
            sleep_time = mn_aw - mn_sl
            clock[mn_sl:mn_aw] = [m + 1 for m in clock[mn_sl:mn_aw]]
            

        guards[guard]["total_sleep"] += sleep_time

        if max_sleep_time < guards[guard]["total_sleep"]:
            max_sleep_time = guards[guard]["total_sleep"]
            max_guard = guard

        i += 2

    max_min_sl = guards[max_guard]["clock"].index(
                    max(guards[max_guard]["clock"]))

    return max_guard, max_min_sl


def main():
    guards = {}
    records = []
    r = None
    action = ""
    guard = None

    for line in sys.stdin:
        line = line[:-1]
        line = line.split(" ", 2)
        
        action = line[2].split(" ")
        if '#' in action[1]:
            guard = int(action[1][1:])
            action = "G"
            guards[guard] = {"total_sleep": 0,
                             "min": None,
                             "clock": [0]*60}
            r = Record(line[0][1:], line[1][:2], line[1][3:-1], action,
                       guard)
        else:
            r = Record(line[0][1:], line[1][:2], line[1][3:-1])

        records.append(r)        
        
    records = sorted(records, key=(lambda x: x.date + x.hour + x.mn))
    #import pprint
    #pprint.pprint([(x.date, x.hour, x.mn, x.action, x.id_g) for x in records])
    
    guard, sleep_time = get_lazzy_guard(records, guards)
   
    #print guard 
    #print sleep_time
    #print guards[guard] 
    print "Result of multiplying guard's id by time asleep: {}".\
          format(guard * sleep_time)


if __name__ == "__main__":
    main()
