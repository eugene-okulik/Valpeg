import datetime

# Исходная дата в строковом формате
date_str = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_obj = datetime.datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

# 1. Печать полного названия месяца
month_name = date_obj.strftime("%B")
print(month_name)  # January

# 2. Печать даты в формате "15.01.2023, 12:05"
formatted_date = date_obj.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)  # 15.01.2023, 12:05
