import time
import os
print(time.time())

current_time = int(time.time())*1000

print(current_time)

print(os.environ['PHPSESSID'])