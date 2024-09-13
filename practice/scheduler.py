# import schedule
# from schedule import every, repeat, run_pending
# import time

# @repeat(every(1).minutes)
# def job():
#     print("I am coding at the moment")
# while True:
#     run_pending()
#     time.sleep(1)

import schedule

def greet(name):
    print("Hello", name)

schedule.every(2).seconds.do(greet, name="Alice")
schedule.every(4).seconds.do(greet, name="Bob")

from schedule import every, repeat

@repeat(every().second, "Earth")
@repeat(every().minute, "Mars")
def hello(planet):
    print("Hello", planet)