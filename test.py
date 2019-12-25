import json
myv = {}
for line in open('mysql_global_variables.sql').readlines():

    line_list = map(lambda x: x.strip('"'), line.strip().split(',')[:2])
    if len(line_list) == 1:
        key = line_list[0]
        value = None
    else:
        # print(line_list)
        key, value = line_list
    myv[key] = value
# print(json.dumps(myv, indent=2))

mys = {}
for line in open('mysql_global_status.sql').readlines():
    line_list = map(lambda x: x.strip('"'), line.strip().split(',')[:2])
    if len(line_list) == 1:
        key = line_list[0]
        value = None
    else:
        # print(line_list)
        key, value = line_list
    mys[key] = value
# print(json.dumps(mys, indent=2))


import time
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp))
print timestamp_toString(time.time())
print time.time()





