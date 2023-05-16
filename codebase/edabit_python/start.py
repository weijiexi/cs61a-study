#  crate a list

# create a list using list comprehension
# [expression for name in sequence if condition]
lst = [x * x for x in range(1, 7) if x % 2 == 0]


# print the list
print(f"lst is: {lst}")

def make_pair(num1, num2):
    """
    Pair Management
    Given two arguments, return a list which contains these two arguments.

    Examples
    make_pair(1, 2) ➞ [1, 2]

    make_pair(51, 21) ➞ [51, 21]

    make_pair(512124, 215) ➞ [512124, 215]
    Notes
    N/A
    """
    return [num1, num2]


def inches_to_feet(inches):
    """
    https://edabit.com/challenge/LRevQqmaH78mwyYXi
    Inches to Feet
    Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.

    Examples
    inches_to_feet(324) ➞ 27

    inches_to_feet(12) ➞ 1

    inches_to_feet(36) ➞ 3
    Notes
    If inches are under 12, return 0.
    12 inches = 1 foot.
    
    FAILED: 0.9166666666666666 should equal 0
    """
    # return inches / 12
    return inches // 12
    
    
