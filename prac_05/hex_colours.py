COLOUR_TO_CODES = {
    "absolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}
print(COLOUR_TO_CODES)
colour_name = input("Enter a colour: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODES[colour_name])
        colour_name = input("Enter a colour: ").lower()
    except KeyError:
        print(f"{colour_name} is not a valid colour.")
        colour_name = input("Enter a colour: ").lower()