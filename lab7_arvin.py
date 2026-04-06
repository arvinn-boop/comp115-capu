def reverse_str(s):
    r = ""
    for c in s:
        r = c + r
    return r

assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0

def remove_duplicates(s):
    r = ""
    for ch in s:
        if ch not in r:
            r = r + ch
    return r

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("pear") == "pear"

def find_index(s, t):
    idx = -1
    for i in range(len(s)):
        if s[i] == t:
            idx = i
            break
    return idx

assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1

days_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

def project_completion_day(day, days_to_completion):
    i = 0
    for d in days_week:
        if d == day:
            break
        i += 1
    return days_week[(i + days_to_completion) % 7]

assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'

def parse_log_line(line):
    parts = line.split()
    ts = parts[0] + " " + parts[1]
    lvl = parts[2][1:-1]
    mod = parts[3]
    msg = ""
    for p in parts[4:]:
        msg += p + " "
    return (ts, lvl, mod, msg.strip())

l1 = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
assert parse_log_line(l1) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

log_string = """2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect"""

lines = log_string.split('\n')
entries = []
for line in lines:
    entries.append(parse_log_line(line))

count_error = 0
for e in entries:
    if e[1] == 'ERROR':
        count_error += 1

print(entries)
print(count_error)
