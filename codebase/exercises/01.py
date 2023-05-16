
"""
# Numbers
2022

# Arithmetic Expressions
2000 + 22
1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)
abs(2299 - 4321)

# Textual Data
'Go Bears'
'Gob' + 'ears'

"""

import urllib.request

url = "https://ucb-course.s3.us-west-1.amazonaws.com/CS61A/shakespeare.txt"

with urllib.request.urlopen(url) as response:
    shakes = response.read().decode('utf-8')
    
"""    
    # Do something with the shakes, e.g.
    print(f'shakes: {shakes}')

# Interesting Data, Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
"""

text = shakes.split()
print(f'len(text): {len(text)}')
print(f'text[:25]: {text[:25]}')
print(f"text.count('the'): {text.count('the')}")
print(f"text.count('forsooth'): {text.count('forsooth')}")
print(f"text.count('Laryn'): {text.count('Laryn')}")
print(f"text.count('Cooper'): {text.count('Cooper')}")
print(f"text.count('Richard'): {text.count('Richard')}")


# Data Format
text.count(',')
text.count(',') / len(text)

# Another Analytical Perspective
words = set(text)
print(f'len(words): {len(words)}')
print(f"'the' in words: {'the' in words}")
print(f"'forsooth' in words: {'forsooth' in words}")
print(f"'computer' in words: {'computer' in words}")
print(f"'Laryn' in words: {'Laryn' in words}")
print(f"'Richard' in words: {'Richard' in words}")

# Operations at Scale
print(f"'draw': {'draw'}")
print(f"'draw'[0]: {'draw'[0]}")
first_letters = {w[0] for w in words}
print(f"first_letters: {first_letters}")

# Combining Operations at Scale
print(f"'draw'[::-1]: {'draw'[::-1]}")
great_four = {w for w in words if w == w[::-1] and len(w) > 4}
print(f"great_four: {great_four}")
eq_four = {w for w in words if w[::-1] in words and len(w) == 4}
print(f"eq_four: {eq_four}")
eq_six = {w for w in words if w[::-1] in words and len(w) == 6}
print(f"eq_six: {eq_six}")
great_six = {w for w in words if w[::-1] in words and len(w) > 6}
print(f"great_six: {great_six}")


# create a list     
