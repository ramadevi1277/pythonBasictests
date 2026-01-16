logs = ['10:00:05', '10:00:20', '10:02:10', '10:02:47', '10:10:00']


def convert_seconds(ts):
    h, m, s = map(int, ts.split(':'))
    return h * 3600 + m* 60 + s

def longest_idle_perios(logs):
    max_idle = 0
    start = end = None

    convert_sec = [convert_seconds(ts) for ts in logs]
    for i in range(1, len(convert_sec)):
        gap = convert_sec[i] - convert_sec[i-1]
        if gap > max_idle:
            max_idle = gap
            start = logs[i-1]
            end = logs[i]

    print(max_idle, start, end)



longest_idle_perios(logs)

