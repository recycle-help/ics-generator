from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
print (c.events)
with open('my.ics', 'w') as f:
    f.write(str(c))