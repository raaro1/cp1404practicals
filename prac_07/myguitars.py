from guitar import Guitar

guitars = []

print("My guitars!")
out_file = open("guitars.csv", "a",newline="")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print(add_guitar, "added.")
    name = input("Name: ")

for guitar in guitars:
    out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
out_file.close()

in_file = open('guitars.csv', 'r')
in_file.readline()
for line in in_file:
    parts = line.strip().split(',')
    name = parts[0]
    year = parts[1]
    cost = parts[2]
    guitar_attributes = Guitar(name, int(year), float(cost))
    guitars.append(guitar_attributes)
in_file.close()


print("\nBefore Sorting\n")
for guitar_attributes in guitars:
    print(guitar_attributes)

guitars.sort()

print("\nAfter Sorting\n")
for guitar_attributes in guitars:
    print(guitar_attributes)