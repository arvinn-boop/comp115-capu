def is_in_list(nums, k):
    for n in nums:
        if n == k:
            return True
    return False

assert is_in_list([4, 5, 6], 5) == True
assert is_in_list([], 3) == False
assert is_in_list([-3, -2, -1, 0], -1) == True

def has_negative(nums):
    for n in nums:
        if n < 0:
            return True
    return False

assert has_negative([1, 2, 3, -4, 5]) == True
assert has_negative([0, 2, 3, 4, 5]) == False

def all_even(nums):
    for n in nums:
        if n % 2 != 0:
            return False
    return True

assert all_even([2, 4, 6, 8]) == True
assert all_even([2, 3, 4]) == False

def count_even_odd(nums):
    even = 0
    odd = 0
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

assert count_even_odd([1, 2, 3, 4, 5, 6]) == [3, 3]
assert count_even_odd([2, 4, 6, 8]) == [4, 0]
assert count_even_odd([1, 3, 5]) == [0, 3]

def temp_category(temps):
    hot = 0
    mild = 0
    cold = 0
    for t in temps:
        if t >= 30:
            hot += 1
        elif t >= 15:
            mild += 1
        else:
            cold += 1
    return [hot, mild, cold]

assert temp_category([32, 28, 15, 12, 35]) == [2, 2, 1]
assert temp_category([10, 5, 0]) == [0, 0, 3]
assert temp_category([20, 25, 30]) == [1, 2, 0]

def mult_category(nums):
    res = []
    for n in nums:
        if n % 2 == 0:
            res.append(2)
        elif n % 3 == 0:
            res.append(3)
        elif n % 5 == 0:
            res.append(5)
        else:
            res.append("O")
    return res

assert mult_category([2, 3, 5, 7]) == [2, 3, 5, "O"]
assert mult_category([4, 9, 10, 11]) == [2, 3, 2, "O"]
assert mult_category([15, 7, 30, 11]) == [3, "O", 2, "O"]

def reverse_list(nums):
    res = []
    for i in range(len(nums)-1, -1, -1):
        res.append(nums[i])
    return res

assert reverse_list([1, 3, 4]) == [4, 3, 1]
assert reverse_list([3, 9, 6]) == [6, 9, 3]

def remove_duplicates(nums):
    res = []
    for n in nums:
        if n not in res:
            res.append(n)
    return res

assert remove_duplicates([1, 3, 3, 4]) == [1, 3, 4]
assert remove_duplicates([1, 1, 3, 4, 3]) == [1, 3, 4]

def my_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

assert my_factorial(0) == 1
assert my_factorial(1) == 1
assert my_factorial(3) == 6
assert my_factorial(5) == 120

def my_fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    res = [0, 1]
    for _ in range(2, n):
        res.append(res[-1] + res[-2])
    return res

assert my_fib(1) == [0]
assert my_fib(2) == [0, 1]
assert my_fib(5) == [0, 1, 1, 2, 3]
assert my_fib(7) == [0, 1, 1, 2, 3, 5, 8]
