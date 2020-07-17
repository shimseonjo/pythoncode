import time,datetime

movieDate=time.strftime('%Y%m%d', time.localtime(time.time()))
print('movieDate type',type(movieDate))

movieDate='2012-02-12'
datetime_obj = datetime.datetime.strptime(movieDate,"%Y-%m-%d").date()
print('datetime_obj type',type(datetime_obj))