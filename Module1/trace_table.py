"""trace_table.py
An example showing variable reassignment to be run with the debugger.
"""

year = 2023

age = year
year = 2006
age = age - year

print("Age is", age)
