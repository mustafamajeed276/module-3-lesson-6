import random
import time
def getrandomdate(enddate, startdate):
    print("generating random date between ", startdate, "and", enddate)
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))
    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("random date is ", getrandomdate(1/1/2000, 12/12/2024))