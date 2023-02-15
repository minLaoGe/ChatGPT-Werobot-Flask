import schedule
import time

def job():
    print("Job is running!")

# 在每个5秒执行一次任务
schedule.every(1200).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)