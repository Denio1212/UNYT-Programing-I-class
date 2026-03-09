"""
Task 6 and after since I had issues with canvas earlier
"""

def decimal_value():
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    dec_value = numerator / denominator
    print(f"{dec_value:.2f}")


def area_of_circle():
    """
    Task 7
    Simple exercise just dealing with floats
    """
    pi = 3.14159
    radius = float(input("Enter a radius: "))
    area = pi * radius * radius
    print(f"The area of the circle is: {area:.2f}")


def round_the_number():
    """
    Task 8
    Using the format method, which is the nicest way for multi-variable printing
    """
    number = float(input("Enter a decimal number: "))
    rounded_number = round(number)
    print("{0}, rounded off to the nearest int is {1}".format(number, rounded_number))

decimal_value()
area_of_circle()
round_the_number()