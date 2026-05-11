
import schedule
import time

def run_pipeline():
    print('Pipeline executed.')

schedule.every().day.at('08:00').do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)
