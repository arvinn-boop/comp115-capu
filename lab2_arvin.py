num = 5
new_num = num * (10 - 5)
print(f"Exercise 1: new_num stores the value of {new_num}.")

dividend = 10
divisor = 3

division_result = dividend / divisor

quotient = dividend // divisor
remainder = dividend % divisor

print(f"""
Exercise 2:
{dividend} ÷ {divisor} = {division_result}   (decimal result)
{dividend} ÷ {divisor} = {quotient} remainder {remainder}
""")

marks = [80.5, 85.3, 76.5, 79.7]
mark_average = (marks[0] + marks[1] + marks[2] + marks[3]) / 4
print(f"Exercise 3: The average mark is {mark_average}!")

print("\nExercise 4")

radius = 2
area = 3.14 * radius * radius
print(f"The area of a circle with radius {radius} is {area}.")

print("\nExercise 5")

day_today = int(input("Enter today's day number: "))
days_trip = int(input("Enter the trip duration in days: "))

day_return = (day_today + days_trip) % 7

print(f"Your trip starts on day {day_today}, lasts {days_trip} days. You are back on day {day_return}.")
