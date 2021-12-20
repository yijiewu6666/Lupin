import datetime
def timestr_standard(time_str):
    now_time = datetime.datetime.now()
    if time_str.endswith('分钟前') or time_str.endswith('小时前') or time_str == '刚刚':
        #strptime是把字符串转换为时间类。strftime是把时间转换为字符串
        time_standard = datetime.datetime.strftime(now_time.date(),'%Y-%m-%d')
    elif time_str.startswith('昨天'):
        time_standard = datetime.datetime.strftime((now_time - datetime.timedelta(days = 1)).date(),'%Y-%m-%d')
    elif time_str.startswith('0') or time_str.startswith('1'):
        time_standard = str(now_time.year) + '-' + time_str
    elif time_str.startswith('20'):
        time_standard = time_str
    return time_standard