weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']

print([[x, weekdays.count(x)] for x in set(weekdays)])

