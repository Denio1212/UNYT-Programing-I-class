"""
Uncer
"""
def uncer():
    try:
        unc_tester = int(input("Please enter your age:"))
    except ValueError:
        raise ValueError("Bro Wtf are you doing")
    if type(unc_tester) == int:
        if unc_tester <= 10:
            print("Haha 67")
        if 10 < unc_tester <= 20:
            print("Oke ur good")
        if 20 < unc_tester <= 28:
            print("You are officially Unc")
        if unc_tester > 28:
            print("Gramps")

uncer()