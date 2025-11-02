from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print(add_guitar, "added.")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\n..snip...\n")

if guitars:
    print("These are my guitars:")
    for i, guitar in enumerate(guitars,1):
        vintage_format = ""
        if guitar.is_vintage():
            vintage_format = " (vintage)"
        print("Guitar {0}: {1.name:>20} ({1.year}), worth $ {1.cost:10,.2f}".format (i, guitar,vintage_format))
else:
    print("No guitars :( Quick, go and buy one!")

