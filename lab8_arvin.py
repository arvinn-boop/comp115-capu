def remove_duplicates(s):
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

def remove_duplicates_set(s):
    res = ''
    seen = set()
    for c in s:
        if c not in seen:
            res += c
            seen.add(c)
    return res

assert remove_duplicates_set("apple") == "aple"

def gem_counting(stones, gems):
    g = set(gems)
    count = 0
    for c in stones:
        if c in g:
            count += 1
    return count

assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("abDFMdm", "af") == 1

def students_id(ids):
    s = set()
    for i in ids:
        s.add(i)
    return len(s)

assert students_id(['002','003','001','012','003','001']) == 4

def students_id_occurrences(ids):
    d = {}
    for i in ids:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

assert students_id_occurrences(['002','003','001','012','003','001']) == {'002':1,'003':2,'001':2,'012':1}

import re
def word_frequency(paragraph):
    words = re.findall(r'\b\w+\b', paragraph)
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

assert word_frequency("I am alive. I am happy.") == {'I':2,'am':2,'alive':1,'happy':1}

def id_name_repo_starred_300k(response_dict):
    d = {}
    if "items" in response_dict:
        for item in response_dict["items"]:
            d[item["id"]] = item["name"]
    return d
