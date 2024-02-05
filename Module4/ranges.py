"""ranges.py"""

for i in range(4):
    print(i)
# Output: '0', '1', '2, '3'

for i in range(2, 6):
    print(i)
# Output: '2', '3', '4, '5'

for i in range(2, 6, 2):
    print(i)
# Output: '2', '4'

treasure = ['p', 'y', 't', 'h', 'o', 'n']

for i in range(len(treasure)):
    print(treasure[i], end='')
print()
# Output: 'python'

for letter in treasure:
    print(letter, end='')
print()
# Output: 'python'