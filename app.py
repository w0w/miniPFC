import schedule
import time

#Import config#

from tasks.sense import capture
from tasks.actuate import recipe

#sense#
schedule.every(1).minutes.do(capture)


#actuate#
schedule.every(1).minutes.do(recipe)

#To-DO - Learn#
while True:
    schedule.run_pending()
    time.sleep(1)
