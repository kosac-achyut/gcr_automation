from datetime import datetime , timedelta
from threading import Timer

x=datetime.today();
y=x.replace(day=x.day,hour=21,minute=29,second=0,microsecond=0) + timedelta(days=1)
delta_t=y-x;

secs = delta_t.seconds + 1

def hello_world():
	print("hello world")

t = Timer(secs,hello_world)
t.start()	
