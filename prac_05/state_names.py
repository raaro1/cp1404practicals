"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    # if state_code in CODE_TO_NAME:
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        for state_abbreviation, full_name  in CODE_TO_NAME.items():
            print(f"{state_abbreviation} is {full_name}.")
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print(f"{state_code} is not a valid state.")
        state_code = input("Enter short state: ").upper()


