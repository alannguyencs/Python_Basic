import datetime

now = datetime.datetime.now()
yesterday = datetime.datetime(2017, 4, 1, 9, 7, 4, 2)

delta = now - yesterday
print ("Now:", now)
print ("Yesterday:", yesterday)
print ("Days:", delta.days)
print ("Seconds:", delta.seconds)
print ("Micro-seconds", delta.microseconds)
print ("Total-seconds", delta.total_seconds())


after = now + datetime.timedelta(days = 2)
print (after)