def rectangle_perimeter(length, width):
    return round((length + width) * 2, 2)

assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01

def convert_american_dollars(usd):
    return round(usd * 1.34, 2)

assert convert_american_dollars(1) == 1.34
assert convert_american_dollars(100) == 134
assert convert_american_dollars(100.05) == 134.07

days_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def back_day_from_trip(day_today, days_trip):
    return days_week[(day_today + days_trip) % 7]

assert back_day_from_trip(3, 5) == "Tuesday"
assert back_day_from_trip(1, 2) == "Thursday"
assert back_day_from_trip(1, 7) == "Tuesday"

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

assert my_sum([1, 4, 5]) == 10
assert my_sum([9, 5]) == 14

def average(nums):
    return round(my_sum(nums) / len(nums), 2)

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 4]) == 2.5
assert average([2, 9, 2]) == 4.33

def sum_of_squares(nums):
    total = 0
    for n in nums:
        total += n ** 2
    return total

assert sum_of_squares([2, 3, 4]) == 29
assert sum_of_squares([2, 4]) == 20
assert sum_of_squares([]) == 0

def add_number(nums, k):
    result = []
    for n in nums:
        result.append(n + k)
    return result

assert add_number([2, 4, 1], 5) == [7, 9, 6]
assert add_number([7, 8], -5) == [2, 3]

def squares(nums):
    result = []
    for n in nums:
        result.append(n ** 2)
    return result

assert squares([2, 3, 4]) == [4, 9, 16]
assert squares([2, 4]) == [4, 16]
assert squares([5, 6, 7]) == [25, 36, 49]
assert squares([]) == []

def repeat_elements(nums):
    result = []
    for n in nums:
        result.append(n)
        result.append(n)
    return result

assert repeat_elements([1, 2, 3, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]
assert repeat_elements([2, 7, 8]) == [2, 2, 7, 7, 8, 8]
assert repeat_elements([]) == []
