import datetime
import math


# 计算当前周数
def getWeekN():
    start = datetime.date(year=2022, month=9, day=5)
    now = datetime.date.today()
    interval = now-start
    today_from_start = interval.days + 1
    # 向上取整；
    return math.ceil(today_from_start/7)

