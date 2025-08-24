# 오늘 날짜

from datetime import datetime

now = datetime.now()

## strftime(): datetime 함수 formating
print(now.strftime("%Y-%m-%d"))