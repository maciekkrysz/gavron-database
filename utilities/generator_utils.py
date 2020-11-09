import random
import time

def rand_string(length):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.sample(s, length ))

def rand_date_in_range(start_date: str, end_date: str):
    format = '%d-%m-%Y'

    start_time = time.mktime(time.strptime(start_date, format))
    end_time = time.mktime(time.strptime(end_date, format))

    result_time = start_time + random.random() * (end_time - start_time)

    return time.strftime(format, time.localtime(result_time))